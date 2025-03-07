# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

# pylint: disable=unused-argument
"""Testing Module nlp.parser."""
import os

import dcr_core.cls_setup
import dcr_core.core_glob
import dcr_core.core_utils
import jellyfish
import pytest
import roman

import dcr.cfg.cls_setup
import dcr.cfg.glob
import dcr.db.cls_run
import dcr.launcher

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test Levenshtein - arabic.
# -----------------------------------------------------------------------------
def test_levenshtein_arabic():
    """Test Levenshtein - arabic."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    upper_limit = 1200

    for prev in range(upper_limit):
        text_curr = f"Page {prev+1} of {str(upper_limit)}"
        text_prev = f"Page {prev} of {str(upper_limit)}"

        distance = jellyfish.levenshtein_distance(
            text_prev,
            text_curr,
        )

        match distance:
            case 1:
                assert True
            case 2:
                assert (prev + 1) % 10 == 0, "prev=" + text_prev + " - curr=" + text_curr
            case 3:
                assert (prev + 1) % 100 == 0, "prev=" + text_prev + " - curr=" + text_curr
            case 4:
                assert (prev + 1) % 1000 == 0, "prev=" + text_prev + " - curr=" + text_curr
            case _:
                assert False, "distance=" + str(distance) + " prev=" + text_prev + " - curr=" + text_curr

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test Levenshtein - roman.
# -----------------------------------------------------------------------------
def test_levenshtein_roman():
    """Test Levenshtein - roman."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    upper_limit = 1200
    upper_limit_roman = roman.toRoman(upper_limit)

    for prev in range(upper_limit):
        text_curr = f"Page {roman.toRoman(prev + 1)} of {upper_limit_roman}"
        text_prev = f"Page {roman.toRoman(prev)} of {upper_limit_roman}"

        distance = jellyfish.levenshtein_distance(
            text_prev,
            text_curr,
        )

        match distance:
            case 1 | 2 | 3 | 4 | 5 | 6 | 7:
                assert True
            case _:
                assert False, "distance=" + str(distance) + " prev=" + text_prev + " - curr=" + text_curr

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_STORE_FROM_PARSER - coverage.
# -----------------------------------------------------------------------------
@pytest.mark.parametrize("verbose_parser", ["all", "none", "text"])
def test_run_action_store_parse_result_in_json_coverage(verbose_parser: str, fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_STORE_FROM_PARSER - coverage."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("pdf_mini", "pdf"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_DELETE_AUXILIARY_FILES, "true"),
            (dcr_core.cls_setup.Setup._DCR_CFG_LT_FOOTER_MAX_LINES, "0"),
            (dcr_core.cls_setup.Setup._DCR_CFG_LT_HEADER_MAX_LINES, "0"),
            (dcr_core.cls_setup.Setup._DCR_CFG_TETML_PAGE, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_VERBOSE_LT_HEADER_FOOTER, "true"),
            (dcr_core.cls_setup.Setup._DCR_CFG_VERBOSE_LT_TOC, "true"),
            (dcr_core.cls_setup.Setup._DCR_CFG_VERBOSE_PARSER, verbose_parser),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDFLIB])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PARSER])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_store_parse_result_in_json_coverage <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox_accepted=(
            [],
            [
                "pdf_mini_1.line.json",
                "pdf_mini_1.word.json",
                "pdf_mini_1.pdf",
            ],
        ),
    )
    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_STORE_FROM_PARSER - coverage - page.
# -----------------------------------------------------------------------------
def test_run_action_store_parse_result_in_json_coverage_page(fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_STORE_FROM_PARSER - coverage."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("pdf_mini", "pdf"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_LT_FOOTER_MAX_LINES, "0"),
            (dcr_core.cls_setup.Setup._DCR_CFG_LT_HEADER_MAX_LINES, "0"),
            (dcr_core.cls_setup.Setup._DCR_CFG_VERBOSE_LT_HEADER_FOOTER, "true"),
            (dcr_core.cls_setup.Setup._DCR_CFG_VERBOSE_LT_TOC, "true"),
            (dcr_core.cls_setup.Setup._DCR_CFG_VERBOSE_PARSER, "text"),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDFLIB])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PARSER])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_STORE_FROM_PARSER - coverage - LineType.
# -----------------------------------------------------------------------------
def test_run_action_store_parse_result_in_json_coverage_line_type(fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_STORE_FROM_PARSER - coverage - LineType."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("p_2_h_0_f_2", "pdf"),
            ("p_2_h_2_f_0", "pdf"),
            ("p_2_h_2_f_2", "pdf"),
            ("p_3_h_0_f_4", "pdf"),
            ("p_3_h_4_f_4", "pdf"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_HEADING, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_TETML_PAGE, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_TETML_WORD, "false"),
        ],
    )
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_DELETE_AUXILIARY_FILES, "false"),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDFLIB])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PARSER])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_store_parse_result_in_json_coverage <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox_accepted=(
            [],
            [
                "p_2_h_0_f_2_1.line.json",
                "p_2_h_0_f_2_1.line.xml",
                "p_2_h_0_f_2_1.pdf",
                "p_2_h_2_f_0_2.line.json",
                "p_2_h_2_f_0_2.line.xml",
                "p_2_h_2_f_0_2.pdf",
                "p_2_h_2_f_2_3.line.json",
                "p_2_h_2_f_2_3.line.xml",
                "p_2_h_2_f_2_3.pdf",
                "p_3_h_0_f_4_4.line.json",
                "p_3_h_0_f_4_4.line.xml",
                "p_3_h_0_f_4_4.pdf",
                "p_3_h_4_f_4_5.line.json",
                "p_3_h_4_f_4_5.line.xml",
                "p_3_h_4_f_4_5.pdf",
            ],
        ),
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_STORE_FROM_PARSER - missing input file.
# -----------------------------------------------------------------------------
def test_run_action_store_parse_result_in_json_missing_input_file(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_STORE_FROM_PARSER - missing input file."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_DELETE_AUXILIARY_FILES, "false"),
        ],
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_store_parse_result_in_json_missing_input_file <=========")

    stem_name_1 = "case_3_pdf_text_route_inbox_pdflib"
    file_ext_1 = "pdf"

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            (stem_name_1, file_ext_1),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDFLIB])

    os.remove(
        dcr_core.core_utils.get_full_name_from_components(dcr_core.core_glob.setup.directory_inbox_accepted, stem_name_1 + "_1.line.xml")
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PARSER])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_STORE_FROM_PARSER - normal.
# -----------------------------------------------------------------------------
def test_run_action_store_parse_result_in_json_normal(fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_STORE_FROM_PARSER - normal."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("pdf_mini", "pdf"),
            ("pdf_scanned_ok", "pdf"),
            ("translating_sql_into_relational_algebra_p01_02", "pdf"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_DELETE_AUXILIARY_FILES, "true"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_HEADING, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_LIST_BULLET, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_LIST_NUMBER, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_TABLE, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_TETML_PAGE, "false"),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDF2IMAGE])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_TESSERACT])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PANDOC])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDFLIB])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PARSER])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_store_parse_result_in_json_normal <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox_accepted=(
            [],
            [
                "pdf_mini_1.line.json",
                "pdf_mini_1.pdf",
                "pdf_mini_1.word.json",
                "pdf_scanned_ok_2_0.line.json",
                "pdf_scanned_ok_2.pdf",
                "pdf_scanned_ok_2_0.word.json",
                "translating_sql_into_relational_algebra_p01_02_3_0.line.json",
                "translating_sql_into_relational_algebra_p01_02_3.pdf",
                "translating_sql_into_relational_algebra_p01_02_3_0.word.json",
            ],
        ),
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_STORE_FROM_PARSER - normal - keep.
# -----------------------------------------------------------------------------
def test_run_action_store_parse_result_in_json_normal_keep(fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_STORE_FROM_PARSER - normal - keep."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("pdf_mini", "pdf"),
            ("pdf_scanned_ok", "pdf"),
            ("translating_sql_into_relational_algebra_p01_02", "pdf"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )
    pytest.helpers.config_params_modify(
        dcr_core.cls_setup.Setup._DCR_CFG_SECTION_CORE_ENV_TEST,
        [
            (dcr_core.cls_setup.Setup._DCR_CFG_DELETE_AUXILIARY_FILES, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_HEADING, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_LIST_BULLET, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_LIST_NUMBER, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_CREATE_EXTRA_FILE_TABLE, "false"),
            (dcr_core.cls_setup.Setup._DCR_CFG_TETML_PAGE, "false"),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDF2IMAGE])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_TESSERACT])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PANDOC])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PDFLIB])

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_PARSER])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_store_parse_result_in_json_normal_keep <=========")

    # TBD
    # if platform.system() != "Windows":
    #     files_expected.append(
    #         "pdf_scanned_03_ok_11.pdf",
    #     )
    pytest.helpers.verify_content_of_inboxes(
        inbox_accepted=(
            [],
            [
                "pdf_mini_1.line.json",
                "pdf_mini_1.line.xml",
                "pdf_mini_1.pdf",
                "pdf_mini_1.word.json",
                "pdf_mini_1.word.xml",
                "pdf_scanned_ok_2.pdf",
                "pdf_scanned_ok_2_1.jpeg",
                "pdf_scanned_ok_2_0.line.json",
                "pdf_scanned_ok_2_0.line.xml",
                "pdf_scanned_ok_2_0.pdf",
                "pdf_scanned_ok_2_0.word.json",
                "pdf_scanned_ok_2_0.word.xml",
                "translating_sql_into_relational_algebra_p01_02_3.pdf",
                "translating_sql_into_relational_algebra_p01_02_3_0.line.json",
                "translating_sql_into_relational_algebra_p01_02_3_0.line.xml",
                "translating_sql_into_relational_algebra_p01_02_3_0.pdf",
                "translating_sql_into_relational_algebra_p01_02_3_0.word.json",
                "translating_sql_into_relational_algebra_p01_02_3_0.word.xml",
                "translating_sql_into_relational_algebra_p01_02_3_1.jpeg",
                "translating_sql_into_relational_algebra_p01_02_3_2.jpeg",
            ],
        ),
    )
    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)
