# pylint: disable=redefined-outer-name
"""Test Configuration and Fixtures.

Setup test libs.cfg.configurations and store fixtures.

Returns:
    [type]: None.
"""

import os
import shutil
import subprocess

import libs.cfg
import libs.db
import pytest

import dcr

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
dcr.initialise_logger()

# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Fixture - Create a new directory.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_mkdir():
    """Fixture Factory: Create a new directory."""

    def _fxtr_mkdir(directory_name: str):
        """
        Fixture: Create a new directory.

        Args:
            directory_name (str): The directory name including path.
        """
        os.mkdir(directory_name)

    return _fxtr_mkdir


# -----------------------------------------------------------------------------
# Fixture - Create a new directory if not existing.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_mkdir_opt(fxtr_mkdir):
    """Fixture Factory: Create a new directory if not existing."""

    def _fxtr_mkdir_opt(directory_name: str):
        """
        Fixture: Create a new directory if not existing.

        Args:
            directory_name (str): The directory name including path.
        """
        if not os.path.isdir(directory_name):
            fxtr_mkdir(directory_name)

    return _fxtr_mkdir_opt


# -----------------------------------------------------------------------------
# Fixture - New empty database and empty inbox.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_new_db_empty_inbox(
    fxtr_mkdir, fxtr_remove, fxtr_remove_opt, fxtr_rmdir, fxtr_rmdir_opt
):
    """Fixture: New empty database and empty inbox directories."""
    dcr.get_config()

    fxtr_remove_opt(libs.db.get_db_file_name())

    fxtr_rmdir_opt(libs.cfg.config[libs.cfg.DCR_CFG_DIRECTORY_INBOX])
    fxtr_mkdir(libs.cfg.config[libs.cfg.DCR_CFG_DIRECTORY_INBOX])
    fxtr_rmdir_opt(libs.cfg.config[libs.cfg.DCR_CFG_DIRECTORY_INBOX_ACCEPTED])
    fxtr_rmdir_opt(libs.cfg.config[libs.cfg.DCR_CFG_DIRECTORY_INBOX_REJECTED])

    if libs.cfg.metadata is not None:
        libs.cfg.metadata.clear()

    dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_CREATE_DB])

    yield

    fxtr_rmdir(libs.cfg.config[libs.cfg.DCR_CFG_DIRECTORY_INBOX])

    fxtr_remove(libs.db.get_db_file_name())


# -----------------------------------------------------------------------------
# Fixture - New empty database, but no inbox directory.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_new_db_no_inbox(fxtr_remove, fxtr_remove_opt, fxtr_rmdir_opt):
    """Fixture: New empty database, but no inbox directory."""
    dcr.get_config()

    fxtr_remove_opt(libs.db.get_db_file_name())

    fxtr_rmdir_opt(libs.cfg.config[libs.cfg.DCR_CFG_DIRECTORY_INBOX])

    if libs.cfg.metadata is not None:
        libs.cfg.metadata.clear()

    dcr.main([libs.cfg.DCR_ARGV_0, libs.cfg.RUN_ACTION_CREATE_DB])

    yield

    fxtr_remove(libs.db.get_db_file_name())


# -----------------------------------------------------------------------------
# Fixture - No database available.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_no_db(fxtr_remove_opt):
    """Fixture: No database available."""
    dcr.get_config()

    fxtr_remove_opt(libs.db.get_db_file_name())

    if libs.cfg.metadata is not None:
        libs.cfg.metadata.clear()

    yield

    fxtr_remove_opt(libs.db.get_db_file_name())


# -----------------------------------------------------------------------------
# Fixture - Delete a file.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_remove():
    """Fixture Factory: Delete a file."""

    def _fxtr_remove(file_name: str):
        """
        Fixture: Delete a file.

        Args:
            file_name (str): File name including path.
        """
        if os.name == libs.cfg.OS_NT:
            try:
                subprocess.check_call(["attrib", "-R", file_name], shell=True)
            except subprocess.CalledProcessError as err:
                print(
                    "Windows command 'attrib -R <file_name>'"
                    + "- error: code='{error_code}' msg='{error_msg}'".replace(
                        "{error_code}",
                        str(err.returncode).replace("{error_msg}", err.output),
                    )
                )
        if os.name == libs.cfg.OS_POSIX:
            try:
                subprocess.check_call(["chattr", "-i", file_name], shell=True)
            except subprocess.CalledProcessError as err:
                print(
                    "Unix command 'chattr -i <file_name>'"
                    + "- error: code='{error_code}' msg='{error_msg}'".replace(
                        "{error_code}",
                        str(err.returncode).replace("{error_msg}", err.output),
                    )
                )

        os.remove(file_name)

    return _fxtr_remove


# -----------------------------------------------------------------------------
# Fixture - Delete a file if existing.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_remove_opt(fxtr_remove):
    """Fixture Factory: Delete a file if existing."""

    def _fxtr_remove_opt(file_name: str):
        """
        Fixture: Delete a file if existing.

        Args:
            file_name (str): File name including path.
        """
        if os.path.isfile(file_name):
            fxtr_remove(file_name)

    return _fxtr_remove_opt


# -----------------------------------------------------------------------------
# Fixture - Delete a directory.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_rmdir():
    """Fixture Factory: Delete a directory."""

    def _fxtr_rmdir(directory_name: str):
        """
        Fixture: Delete a directory.

        Args:
            directory_name (str): The directory name including path.
        """
        if os.name == libs.cfg.OS_NT:
            try:
                subprocess.check_call(["attrib", "-R", "*"], shell=True)
            except subprocess.CalledProcessError as err:
                print(
                    "Windows command 'attrib -R <file_name>'"
                    + "- error: code='{error_code}' msg='{error_msg}'".replace(
                        "{error_code}",
                        str(err.returncode).replace("{error_msg}", err.output),
                    )
                )
        if os.name == libs.cfg.OS_POSIX:
            try:
                subprocess.check_call(["chattr", "-i", "*"], shell=True)
            except subprocess.CalledProcessError as err:
                print(
                    "Unix command 'chattr -i <file_name>'"
                    + "- error: code='{error_code}' msg='{error_msg}'".replace(
                        "{error_code}",
                        str(err.returncode).replace("{error_msg}", err.output),
                    )
                )

        shutil.rmtree(directory_name)

    return _fxtr_rmdir


# -----------------------------------------------------------------------------
# Fixture - Delete a directory if existing.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_rmdir_opt(fxtr_rmdir):
    """Fixture Factory: Delete a directory if existing."""

    def _fxtr_rmdir_opt(directory_name: str):
        """
        Fixture: Delete a directory if existing.

        Args:
            directory_name (str): The directory name including path.
        """
        if os.path.isdir(directory_name):
            fxtr_rmdir(directory_name)

    return _fxtr_rmdir_opt
