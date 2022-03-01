# pylint: disable=unused-argument
"""Testing Module libs.inbox."""
import shutil

import libs.cfg
import libs.db
import pytest

import dcr

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PDF_2_IMAGE.
# -----------------------------------------------------------------------------
def test_run_action_pdf_2_image(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PDF_2_IMAGE."""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    current_document_id, current_no = pytest.helpers.run_action_setup()

    # -------------------------------------------------------------------------
    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "pdf_scanned_ok", "pdf"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_no = pytest.helpers.run_action_pdf_2_image(
        libs.cfg.RUN_ACTION_PDF_2_IMAGE,
        "pdf_scanned_ok_1",
        current_no,
    )

    # -------------------------------------------------------------------------
    shutil.rmtree(libs.cfg.directory_inbox)

    with pytest.raises(SystemExit) as expt:
        current_no = pytest.helpers.run_action_pdf_2_image(
            libs.cfg.RUN_ACTION_PDF_2_IMAGE,
            "pdf_scanned_ok_1",
            current_no,
        )

    assert expt.type == SystemExit, "inbox directory missing"
    assert expt.value.code == 1, "inbox directory missing"

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
    libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
    libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug(libs.cfg.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - duplicates allowed.
# -----------------------------------------------------------------------------
@pytest.mark.issue
def test_run_action_process_inbox_duplicates(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - duplicates allowed."""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    current_document_id, current_no = pytest.helpers.run_action_setup()

    # -------------------------------------------------------------------------
    pytest.helpers.store_config_param(
        libs.cfg.DCR_CFG_SECTION, libs.cfg.DCR_CFG_IGNORE_DUPLICATES, "true"
    )

    stem_name =  "pdf_text_ok"
    file_extension = "pdf"

    libs.cfg.logger.debug("Document #%i : %s.%s",current_document_id,stem_name,file_extension)

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), stem_name, file_extension),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    libs.cfg.logger.debug("Document #%i : %s.%s", current_document_id, stem_name, file_extension)

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), stem_name, file_extension),
        current_no,
    )

    # -------------------------------------------------------------------------
    shutil.rmtree(libs.cfg.directory_inbox)

    with pytest.raises(SystemExit) as expt:
        dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_PROCESS_INBOX])

    assert expt.type == SystemExit, "inbox directory missing"
    assert expt.value.code == 1, "inbox directory missing"

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
    libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
    libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug(libs.cfg.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - no duplicates allowed.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_no_duplicates(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - no duplicates allowed."""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    current_document_id, current_no = pytest.helpers.run_action_setup()

    # -------------------------------------------------------------------------
    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "doc_ok", "doc"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "docx_ok", "docx"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "htm_ok", "htm"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "html_ok", "html"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "jpeg_pdf_text_ok_1", "jpeg"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "jpg_pdf_text_ok_1", "jpg"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "odt_ok", "odt"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "pdf_scanned_ok", "pdf"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "pdf_text_ok", "pdf"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_rejected), "pdf_text_ok_protected", "pdf"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_rejected), "pdf_wrong_format", "pdf"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "png_pdf_text_ok_1", "png"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "rtf_ok", "rtf"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "tiff_pdf_text_ok_1", "tiff"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "txt_ok", "txt"),
        current_no,
    )

    # -------------------------------------------------------------------------
    current_document_id += 2

    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_rejected), "unknown_file_extension", "xxx"),
        current_no,
    )

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
    libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
    libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug(libs.cfg.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - README.md
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_readme_md(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - README.md"""
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    # -------------------------------------------------------------------------
    current_document_id, current_no = pytest.helpers.run_action_setup()

    # -------------------------------------------------------------------------
    current_no = pytest.helpers.run_action_process_inbox(
        libs.cfg.RUN_ACTION_PROCESS_INBOX,
        current_document_id,
        (str(libs.cfg.directory_inbox_accepted), "README.md", None),
        current_no,
    )

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug("Directory: inbox          - Number of files=%i", current_no[0])
    libs.cfg.logger.debug("Directory: inbox_accepted - Number of files=%i", current_no[1])
    libs.cfg.logger.debug("Directory: inbox_rejected - Number of files=%i", current_no[2])

    # -------------------------------------------------------------------------
    libs.cfg.logger.debug(libs.cfg.LOGGER_END)
