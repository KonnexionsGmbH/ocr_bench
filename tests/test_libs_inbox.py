# pylint: disable=unused-argument
"""Testing Module libs.inbox."""

import libs.cfg
import libs.db
import pytest

import dcr

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test RUN_ACTION_ALL_COMPLETE - normal.
# -----------------------------------------------------------------------------
def test_run_action_all_normal(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_ALL_COMPLETE - normal."""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    stem_name: str = "pdf_scanned_ok"
    file_ext: str = "pdf"

    pytest.helpers.copy_files_from_pytest_2_dir([(stem_name, file_ext)], libs.cfg.directory_inbox)

    # -------------------------------------------------------------------------
    dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_ALL_COMPLETE])

    # -------------------------------------------------------------------------
    child_no: int = 1
    document_id: int = 1
    no_files_expected = (0, 2, 0)

    file_p_i = (
        libs.cfg.directory_inbox_accepted,
        [stem_name, str(document_id)],
        file_ext,
    )

    file_p_2_i = (
        libs.cfg.directory_inbox_accepted,
        [stem_name, str(document_id), str(child_no)],
        libs.cfg.pdf2image_type,
    )

    files_to_be_checked = [
        file_p_i,
        file_p_2_i,
    ]

    pytest.helpers.verify_content_inboxes(
        files_to_be_checked,
        no_files_expected,
    )


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PDF_2_IMAGE - normal.
# -----------------------------------------------------------------------------
def test_run_action_pdf_2_image_normal(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PDF_2_IMAGE - normal."""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    stem_name: str = "pdf_scanned_ok"
    file_ext: str = "pdf"

    pytest.helpers.copy_files_from_pytest_2_dir([(stem_name, file_ext)], libs.cfg.directory_inbox)

    # -------------------------------------------------------------------------
    dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_PROCESS_INBOX])

    # -------------------------------------------------------------------------
    document_id: int = 1
    no_files_expected = (0, 1, 0)

    file_p_i = (
        libs.cfg.directory_inbox_accepted,
        [stem_name, str(document_id)],
        file_ext,
    )

    files_to_be_checked = [
        file_p_i,
    ]

    pytest.helpers.verify_content_inboxes(
        files_to_be_checked,
        no_files_expected,
    )

    # -------------------------------------------------------------------------
    dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_PDF_2_IMAGE])

    # -------------------------------------------------------------------------
    child_no: int = 1
    no_files_expected = (0, 2, 0)

    file_p_2_i = (
        libs.cfg.directory_inbox_accepted,
        [stem_name, str(document_id), str(child_no)],
        libs.cfg.pdf2image_type,
    )

    files_to_be_checked = [
        file_p_i,
        file_p_2_i,
    ]

    pytest.helpers.verify_content_inboxes(
        files_to_be_checked,
        no_files_expected,
    )

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug(libs.cfg.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - normal.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_normal(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - normal."""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_from_pytest_2_dir(
        [
            ("doc_ok", "doc"),
            ("docx_ok", "docx"),
            ("jpeg_pdf_text_ok_1", "jpeg"),
            ("jpg_pdf_text_ok_1", "jpg"),
            ("odt_ok", "odt"),
            ("pdf_text_ok", "pdf"),
            ("png_pdf_text_ok_1", "png"),
            ("README.md", None),
            ("rtf_ok", "rtf"),
            ("tiff_pdf_text_ok_2", "tiff"),
            ("txt_ok", "txt"),
        ],
        libs.cfg.directory_inbox,
    )

    # -------------------------------------------------------------------------
    dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_PROCESS_INBOX])

    # -------------------------------------------------------------------------
    no_files_expected = (1, 10, 0)

    files_to_be_checked = [
        (
            libs.cfg.directory_inbox_accepted,
            ["doc_ok", "1"],
            "doc",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["docx_ok", "3"],
            "docx",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["jpeg_pdf_text_ok_1", "5"],
            "jpeg",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["jpg_pdf_text_ok_1", "7"],
            "jpg",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["odt_ok", "9"],
            "odt",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["pdf_text_ok", "11"],
            "pdf",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["png_pdf_text_ok_1", "13"],
            "png",
        ),
        (
            libs.cfg.directory_inbox,
            ["README.md"],
            None,
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["rtf_ok", "15"],
            "rtf",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["tiff_pdf_text_ok_2", "17"],
            "tiff",
        ),
        (
            libs.cfg.directory_inbox_accepted,
            ["txt_ok", "19"],
            "txt",
        ),
    ]

    pytest.helpers.verify_content_inboxes(
        files_to_be_checked,
        no_files_expected,
    )

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug(libs.cfg.LOGGER_END)


# # -----------------------------------------------------------------------------
# # Test RUN_ACTION_PROCESS_INBOX - duplicates allowed.
# # -----------------------------------------------------------------------------
# def test_run_action_process_inbox_duplicates(fxtr_setup_empty_db_and_inbox):
#     """Test RUN_ACTION_PROCESS_INBOX - duplicates allowed."""
#     libs.cfg.logger.debug(libs.cfg.LOGGER_START)
#
#     # -------------------------------------------------------------------------
#     current_document_id, current_no = pytest.helpers.run_action_setup()
#
#     # -------------------------------------------------------------------------
#     pytest.helpers.store_config_param(
#         libs.cfg.DCR_CFG_SECTION, libs.cfg.DCR_CFG_IGNORE_DUPLICATES, "true"
#     )
#
#     stem_name = "pdf_text_ok"
#     file_extension = "pdf"
#
#     libs.cfg.logger.debug("Document #%i : %s.%s", current_document_id, stem_name, file_extension)
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), stem_name, file_extension),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     libs.cfg.logger.debug("Document #%i : %s.%s", current_document_id, stem_name, file_extension)
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), stem_name, file_extension),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     shutil.rmtree(libs.cfg.directory_inbox)
#
#     with pytest.raises(SystemExit) as expt:
#         dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_PROCESS_INBOX])
#
#     assert expt.type == SystemExit, "inbox directory missing"
#     assert expt.value.code == 1, "inbox directory missing"
#
#     # -------------------------------------------------------------------------
#     libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
#     libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
#     libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])
#
#     # -------------------------------------------------------------------------
#     libs.cfg.logger.debug(libs.cfg.LOGGER_END)
#
#
# # -----------------------------------------------------------------------------
# # Test RUN_ACTION_PROCESS_INBOX - no duplicates allowed.
# # -----------------------------------------------------------------------------
# def test_run_action_process_inbox_no_duplicates(fxtr_setup_empty_db_and_inbox):
#     """Test RUN_ACTION_PROCESS_INBOX - no duplicates allowed."""
#     libs.cfg.logger.debug(libs.cfg.LOGGER_START)
#
#     # -------------------------------------------------------------------------
#     current_document_id, current_no = pytest.helpers.run_action_setup()
#
#     # -------------------------------------------------------------------------
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "doc_ok", "doc"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "docx_ok", "docx"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "htm_ok", "htm"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "html_ok", "html"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "jpeg_pdf_text_ok_1", "jpeg"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "jpg_pdf_text_ok_1", "jpg"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "odt_ok", "odt"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "pdf_scanned_ok", "pdf"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "pdf_text_ok", "pdf"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_rejected), "pdf_text_ok_protected", "pdf"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_rejected), "pdf_wrong_format", "pdf"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "png_pdf_text_ok_1", "png"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "rtf_ok", "rtf"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "tiff_pdf_text_ok_1", "tiff"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "txt_ok", "txt"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     current_document_id += 2
#
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_rejected), "unknown_file_extension", "xxx"),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
#     libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
#     libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])
#
#     # -------------------------------------------------------------------------
#     libs.cfg.logger.debug(libs.cfg.LOGGER_END)
#
#
# # -----------------------------------------------------------------------------
# # Test RUN_ACTION_PROCESS_INBOX - README.md
# # -----------------------------------------------------------------------------
# def test_run_action_process_inbox_readme_md(fxtr_setup_empty_db_and_inbox):
#     """Test RUN_ACTION_PROCESS_INBOX - README.md"""
#     libs.cfg.logger.debug(libs.cfg.LOGGER_START)
#
#     # -------------------------------------------------------------------------
#     current_document_id, current_no = pytest.helpers.run_action_setup()
#
#     # -------------------------------------------------------------------------
#     current_no = pytest.helpers.run_action_process_inbox(
#         libs.cfg.RUN_ACTION_PROCESS_INBOX,
#         current_document_id,
#         (str(libs.cfg.directory_inbox_accepted), "README.md", None),
#         current_no,
#     )
#
#     # -------------------------------------------------------------------------
#     libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
#     libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
#     libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])
#
#     # -------------------------------------------------------------------------
#     libs.cfg.logger.debug(libs.cfg.LOGGER_END)
