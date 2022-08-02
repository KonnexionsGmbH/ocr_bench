"""Module nlp.parser: Store the document structure from the parser result."""
import os
import time

import cfg.glob
import db.cls_action
import db.cls_document
import db.cls_run
import utils

import dcr_core.cls_nlp_core
import dcr_core.cls_text_parser
import dcr_core.core_glob
import dcr_core.core_utils
import dcr_core.processing

# -----------------------------------------------------------------------------
# Global variables.
# -----------------------------------------------------------------------------
TETML_TYPE_LINE = "line"
TETML_TYPE_PAGE = "page"
TETML_TYPE_WORD = "word"


# -----------------------------------------------------------------------------
# Parse the TETML files (step: s_p_j).
# -----------------------------------------------------------------------------
def parse_tetml() -> None:
    """Parse the TETML files.

    TBD
    """
    cfg.glob.logger.debug(cfg.glob.LOGGER_START)

    for (tetml_type, action_code, is_parsing_line, is_parsing_page, is_parsing_word,) in (
        (
            TETML_TYPE_LINE,
            db.cls_run.Run.ACTION_CODE_PARSER_LINE,
            True,
            False,
            False,
        ),
        (
            TETML_TYPE_PAGE,
            db.cls_run.Run.ACTION_CODE_PARSER_PAGE,
            False,
            True,
            False,
        ),
        (
            TETML_TYPE_WORD,
            db.cls_run.Run.ACTION_CODE_PARSER_WORD,
            False,
            False,
            True,
        ),
    ):
        utils.progress_msg(f"Start of processing for tetml type '{tetml_type}'")

        dcr_core.core_glob.setup.is_parsing_line = is_parsing_line
        dcr_core.core_glob.setup.is_parsing_page = is_parsing_page
        dcr_core.core_glob.setup.is_parsing_word = is_parsing_word

        with cfg.glob.db_core.db_orm_engine.begin() as conn:
            rows = db.cls_action.Action.select_action_by_action_code(conn=conn, action_code=action_code)

            for row in rows:
                # ------------------------------------------------------------------
                # Processing a single document
                # ------------------------------------------------------------------
                cfg.glob.start_time_document = time.perf_counter_ns()

                cfg.glob.run.run_total_processed_to_be += 1

                cfg.glob.action_curr = db.cls_action.Action.from_row(row)

                if cfg.glob.action_curr.action_status == db.cls_document.Document.DOCUMENT_STATUS_ERROR:
                    cfg.glob.run.total_status_error += 1
                else:
                    cfg.glob.run.total_status_ready += 1

                cfg.glob.document = db.cls_document.Document.from_id(
                    id_document=cfg.glob.action_curr.action_id_document
                )

                parse_tetml_file()

            conn.close()
        utils.progress_msg(f"End   of processing for tetml type '{tetml_type}'")

    utils.show_statistics_total()

    cfg.glob.logger.debug(cfg.glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Parse the TETML file (step: s_p_j).
# -----------------------------------------------------------------------------
# noinspection PyArgumentList
def parse_tetml_file() -> None:
    """Parse the TETML file.

    TBD
    """
    full_name_curr = cfg.glob.action_curr.get_full_name()

    file_name_next = cfg.glob.action_curr.get_stem_name() + "." + dcr_core.core_glob.FILE_TYPE_JSON
    full_name_next = dcr_core.core_utils.get_full_name(
        cfg.glob.action_curr.action_directory_name,
        file_name_next,
    )

    if dcr_core.core_glob.setup.is_parsing_line:
        status = db.cls_document.Document.DOCUMENT_STATUS_START
    else:
        status = db.cls_document.Document.DOCUMENT_STATUS_END

    cfg.glob.action_next = db.cls_action.Action(
        action_code=db.cls_run.Run.ACTION_CODE_TOKENIZE,
        id_run_last=cfg.glob.run.run_id,
        directory_name=cfg.glob.action_curr.action_directory_name,
        directory_type=cfg.glob.action_curr.action_directory_type,
        file_name=file_name_next,
        id_document=cfg.glob.action_curr.action_id_document,
        id_parent=cfg.glob.action_curr.action_id,
        no_pdf_pages=cfg.glob.action_curr.action_no_pdf_pages,
        status=status,
    )

    (error_code, error_msg) = dcr_core.processing.parser_process(
        full_name_in=cfg.glob.action_curr.get_full_name(),
        full_name_out=cfg.glob.action_next.get_full_name(),
        document_id=cfg.glob.action_curr.action_id_document,
        file_name_orig=cfg.glob.document.document_file_name,
        no_pdf_pages=cfg.glob.action_curr.action_no_pdf_pages,
    )
    if (error_code, error_msg) != dcr_core.core_glob.RETURN_OK:
        cfg.glob.action_curr.finalise_error(error_code, error_msg)
        return

    cfg.glob.run.run_total_processed_ok += 1

    if dcr_core.core_glob.setup.is_parsing_line:
        if (
            dcr_core.core_glob.line_type_headers_footers.no_lines_footer
            != 0  # pylint: disable=too-many-boolean-expressions
            or dcr_core.core_glob.line_type_headers_footers.no_lines_header != 0
            or dcr_core.core_glob.line_type_list_bullet.no_lists != 0
            or dcr_core.core_glob.line_type_list_number.no_lists != 0
            or dcr_core.core_glob.line_type_table.no_tables != 0
            or dcr_core.core_glob.line_type_toc.no_lines_toc != 0
        ):
            cfg.glob.document.document_no_lines_footer = dcr_core.core_glob.line_type_headers_footers.no_lines_footer
            cfg.glob.document.document_no_lines_header = dcr_core.core_glob.line_type_headers_footers.no_lines_header
            cfg.glob.document.document_no_lines_toc = dcr_core.core_glob.line_type_toc.no_lines_toc
            cfg.glob.document.document_no_lists_bullet = dcr_core.core_glob.line_type_list_bullet.no_lists
            cfg.glob.document.document_no_lists_number = dcr_core.core_glob.line_type_list_number.no_lists
            cfg.glob.document.document_no_tables = dcr_core.core_glob.line_type_table.no_tables
            cfg.glob.document.persist_2_db()  # type: ignore

    cfg.glob.action_next.action_file_size_bytes = (os.path.getsize(full_name_next),)

    cfg.glob.action_curr.finalise()

    utils.delete_auxiliary_file(full_name_curr)
