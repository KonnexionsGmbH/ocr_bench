# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

# pylint: disable=unused-argument
"""Testing Module pp.inbox."""
import os.path
import pathlib
import shutil

import dcr_core.core_glob
import dcr_core.core_utils
import pytest

import dcr.cfg.cls_setup
import dcr.cfg.glob
import dcr.db.cls_db_core
import dcr.db.cls_run
import dcr.launcher

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - accepted - duplicate.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_accepted_duplicate(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - accepted duplicate."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    stem_name_1 = "pdf_text_ok"
    file_ext = "pdf"

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            (stem_name_1, file_ext),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    stem_name_2 = "pdf_text_ok_1"

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[(stem_name_1, file_ext)], target_path=dcr_core.core_glob.setup.directory_inbox_accepted
    )

    os.rename(
        dcr_core.core_utils.get_full_name_from_components(dcr_core.core_glob.setup.directory_inbox_accepted, stem_name_1 + "." + file_ext),
        dcr_core.core_utils.get_full_name_from_components(dcr_core.core_glob.setup.directory_inbox_accepted, stem_name_2 + "." + file_ext),
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )

    # -------------------------------------------------------------------------
    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_process_inbox_accepted_duplicate <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox=(
            [],
            [
                stem_name_1 + "." + file_ext,
            ],
        ),
        inbox_accepted=(
            [],
            [
                stem_name_2 + "." + file_ext,
            ],
        ),
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - french.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_french(fxtr_setup_empty_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - French."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    db_initial_data_file_path = pathlib.Path(dcr_core.core_glob.setup.db_initial_data_file)
    db_initial_data_file_path_directory = os.path.dirname(db_initial_data_file_path)
    db_initial_data_file_path_file_name = os.path.basename(db_initial_data_file_path)

    db_initial_data_file_path_file_name_test = "db_initial_data_file_french.json"

    # copy test file
    shutil.copy(
        dcr_core.core_utils.get_full_name_from_components(
            pytest.helpers.get_test_inbox_directory_name(), db_initial_data_file_path_file_name_test
        ),
        dcr_core.core_utils.get_full_name_from_components(db_initial_data_file_path_directory, db_initial_data_file_path_file_name),
    )

    dcr.cfg.glob.db_core = dcr.db.cls_db_core.DBCore(is_admin=True)

    dcr.cfg.glob.db_core.create_database()

    # -------------------------------------------------------------------------
    # Copy language subdirectory
    pytest.helpers.copy_directories_4_pytest_2_dir(source_directories=["french"], target_dir=str(dcr_core.core_glob.setup.directory_inbox))

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "before"),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_process_inbox_french <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox=(
            ["french"],
            [],
        ),
        inbox_accepted=(
            [],
            [
                "1_docx_french_ok.docx",
                "2_pdf_french_ok.jpg",
                "3_pdf_french_ok.pdf",
                "4_pdf_french_scanned.pdf",
            ],
        ),
    )

    # -------------------------------------------------------------------------
    base_directory = str(dcr_core.core_glob.setup.directory_inbox)
    language_directory_name = str(dcr_core.core_utils.get_full_name_from_components(base_directory, pathlib.Path("french")))

    assert os.path.isdir(dcr_core.core_utils.get_os_independent_name(base_directory)), (
        "base directory '" + base_directory + "' after processing missing"
    )

    assert os.path.isdir(dcr_core.core_utils.get_os_independent_name(language_directory_name)), (
        "language directory '" + language_directory_name + "' after processing missing"
    )

    assert len(os.listdir(language_directory_name)) == 0, (
        str(len(os.listdir(language_directory_name))) + " files still found after processing"
    )

    # -------------------------------------------------------------------------
    # Check empty language subdirectory
    # TBD

    # -------------------------------------------------------------------------
    # Test not language English in document
    # TBD

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - ignore duplicates.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_ignore_duplicates(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - ignore duplicates."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("pdf_text_ok", "pdf"),
            ("pdf_text_ok_protected", "pdf"),
        ],
        target_path=dcr_core.core_glob.setup.directory_inbox,
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_IGNORE_DUPLICATES, "true"),
        ],
    )

    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_process_inbox_ignore_duplicates <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox_accepted=(
            [],
            [
                "pdf_text_ok.pdf",
                "pdf_text_ok_protected.pdf",
            ],
        ),
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - rejected.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_rejected(fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - rejected."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    fxtr_rmdir_opt(dcr_core.core_glob.setup.directory_inbox_accepted)

    fxtr_rmdir_opt(dcr_core.core_glob.setup.directory_inbox_rejected)

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("pdf_text_ok", "pdf"),
            ("pdf_text_ok_protected", "pdf"),
            ("pdf_wrong_format", "pdf"),
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

    # -------------------------------------------------------------------------
    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_process_inbox_rejected <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox=(
            [],
            [],
        ),
        inbox_accepted=(
            [],
            [
                "pdf_text_ok_1.pdf",
            ],
        ),
        inbox_rejected=(
            [],
            [
                "pdf_text_ok_protected_2.pdf",
                "pdf_wrong_format_3.pdf",
            ],
        ),
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - rejected - duplicate.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_rejected_duplicate(fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - rejected duplicate."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    stem_name_1 = "pdf_wrong_format"
    file_ext = "pdf"

    pytest.helpers.copy_files_4_pytest_2_dir(source_files=[(stem_name_1, file_ext)], target_path=dcr_core.core_glob.setup.directory_inbox)

    stem_name_2 = "pdf_wrong_format_1"

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[(stem_name_1, file_ext)], target_path=dcr_core.core_glob.setup.directory_inbox_rejected
    )

    os.rename(
        dcr_core.core_utils.get_full_name_from_components(dcr_core.core_glob.setup.directory_inbox_rejected, stem_name_1 + "." + file_ext),
        dcr_core.core_utils.get_full_name_from_components(dcr_core.core_glob.setup.directory_inbox_rejected, stem_name_2 + "." + file_ext),
    )

    # -------------------------------------------------------------------------
    pytest.helpers.config_params_modify(
        dcr.cfg.cls_setup.Setup._DCR_CFG_SECTION_ENV_TEST,
        [
            (dcr.cfg.cls_setup.Setup._DCR_CFG_DOC_ID_IN_FILE_NAME, "after"),
        ],
    )

    # -------------------------------------------------------------------------
    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_process_inbox_rejected_duplicate <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox=(
            [],
            [
                stem_name_1 + "." + file_ext,
            ],
        ),
        inbox_rejected=(
            [],
            [
                stem_name_2 + "." + file_ext,
            ],
        ),
    )

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Test RUN_ACTION_PROCESS_INBOX - rejected - 901.
# -----------------------------------------------------------------------------
def test_run_action_process_inbox_rejected_901(fxtr_rmdir_opt, fxtr_setup_empty_db_and_inbox):
    """Test RUN_ACTION_PROCESS_INBOX - rejected - 901."""
    dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

    # -------------------------------------------------------------------------
    fxtr_rmdir_opt(dcr_core.core_glob.setup.directory_inbox_accepted)

    fxtr_rmdir_opt(dcr_core.core_glob.setup.directory_inbox_rejected)

    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[
            ("unknown_file_extension", "xxx"),
            ("unknown_file_extension_protected", "xxx"),
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

    # -------------------------------------------------------------------------
    dcr.launcher.main([dcr.launcher.DCR_ARGV_0, dcr.db.cls_run.Run.ACTION_CODE_INBOX])

    # -------------------------------------------------------------------------
    dcr_core.core_glob.logger.info("=========> test_run_action_process_inbox_rejected <=========")

    pytest.helpers.verify_content_of_inboxes(
        inbox=(
            [],
            [],
        ),
        inbox_accepted=(
            [],
            [],
        ),
        inbox_rejected=(
            [],
            [
                "unknown_file_extension_1.xxx",
                "unknown_file_extension_protected_2.xxx",
            ],
        ),
    )
