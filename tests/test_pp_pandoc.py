# pylint: disable=unused-argument
"""Testing Module pp.pandoc_dcr."""
import cfg.cls_setup
import cfg.glob
import db.cls_run
import launcher
import pytest

import dcr_core.core_glob

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test RUN_ACTION_NON_PDF_2_PDF - coverage.
# -----------------------------------------------------------------------------
def test_run_action_non_pdf_2_pdf_coverage(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_NON_PDF_2_PDF - coverage."""
    cfg.glob.logger.debug(cfg.glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("p_2_h_0_f_2", "docx"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    launcher.main([launcher.DCR_ARGV_0, db.cls_run.Run.ACTION_CODE_INBOX])

    launcher.main([launcher.DCR_ARGV_0, db.cls_run.Run.ACTION_CODE_PANDOC])

    # -------------------------------------------------------------------------
    cfg.glob.logger.debug(cfg.glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_NON_PDF_2_PDF - normal - duplicate.
# -----------------------------------------------------------------------------
def test_run_action_non_pdf_2_pdf_normal_duplicate(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_NON_PDF_2_PDF - normal - duplicate."""
    cfg.glob.logger.debug(cfg.glob.LOGGER_START)

    # -------------------------------------------------------------------------
    cfg.glob.logger.info("=========> test_run_action_non_pdf_2_pdf_normal_duplicate <=========")

    stem_name_1 = "docx_ok"
    file_ext_1 = "docx"

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            (stem_name_1, file_ext_1),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )

    # -------------------------------------------------------------------------
    stem_name_2 = "docx_ok_1"
    file_ext_2 = "pdf"

    pytest.helpers.help_run_action_all_complete_duplicate_file(file_ext_1, file_ext_2, stem_name_1, stem_name_2)

    # -------------------------------------------------------------------------
    cfg.glob.logger.debug(cfg.glob.LOGGER_END)
