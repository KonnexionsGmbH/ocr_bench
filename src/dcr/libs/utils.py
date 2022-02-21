"""Module utils: Helper functions."""
import datetime
import hashlib
import subprocess
import sys
import traceback

import libs.cfg
import libs.utils


# -----------------------------------------------------------------------------
# Get the SHA256 hash string of a file.
# -----------------------------------------------------------------------------
def get_sha256(file_name: str) -> str:
    """Get the SHA256 hash string of a file.

    Args:
        file_name (str): File name.

    Returns:
        str: SHA256 hash string.
    """
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    sha256_hash = hashlib.sha256()

    with open(file_name, "rb") as file:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    libs.cfg.logger.debug(libs.cfg.LOGGER_END)

    return sha256_hash.hexdigest()


# -----------------------------------------------------------------------------
# Create a progress message.
# -----------------------------------------------------------------------------
def progress_msg(msg: str) -> None:
    """Create a progress message.

    Args:
        msg (str): Progress message.
    """
    if libs.cfg.is_verbose:
        final_msg: str = (
            libs.cfg.LOGGER_PROGRESS_UPDATE + str(datetime.datetime.now()) + " : " + msg + "."
        )

        print(final_msg)

        libs.cfg.logger.debug(final_msg)


# -----------------------------------------------------------------------------
# Create a progress message: connected to database.
# -----------------------------------------------------------------------------
def progress_msg_connected() -> None:
    """Create a progress message: connected to database."""
    if libs.cfg.is_verbose:
        print("")
        progress_msg(
            "User '"
            + libs.cfg.db_current_user
            + "' is now connected to database '"
            + libs.cfg.db_current_database
            + "'"
        )


# -----------------------------------------------------------------------------
# Create a progress message: disconnected from database.
# -----------------------------------------------------------------------------
def progress_msg_disconnected() -> None:
    """Create a progress message: disconnected from database."""
    if libs.cfg.is_verbose:
        print("")
        libs.utils.progress_msg(
            "User '"
            + libs.cfg.db_current_user
            + "' is now disconnected from database '"
            + libs.cfg.db_current_database
            + "'"
        )


# -----------------------------------------------------------------------------
# Create a progress message with empty line before.
# -----------------------------------------------------------------------------
def progress_msg_empty_before(msg: str) -> None:
    """Create a progress message.

    Args:
        msg (str): Progress message.
    """
    if libs.cfg.is_verbose:
        print("")
        progress_msg(msg)


# -----------------------------------------------------------------------------
# Start the database Docker container.
# -----------------------------------------------------------------------------
def start_db_docker_container() -> None:
    """Start the database Docker container."""
    try:
        subprocess.run(
            ["docker", "start", libs.cfg.config[libs.cfg.DCR_CFG_DB_DOCKER_CONTAINER]], check=True
        )
    except subprocess.CalledProcessError as err:
        libs.utils.terminate_fatal(
            "The Docker Container '"
            + libs.cfg.config[libs.cfg.DCR_CFG_DB_DOCKER_CONTAINER]
            + "' cannot be started - error="
            + str(err),
        )


# -----------------------------------------------------------------------------
# Terminate the application immediately.
# -----------------------------------------------------------------------------
def terminate_fatal(error_msg: str) -> None:
    """Terminate the application immediately.

    Args:
        error_msg (str): Error message.
    """
    libs.cfg.logger.debug(libs.cfg.LOGGER_START)

    print("")
    print(libs.cfg.LOGGER_FATAL_HEAD)
    print(libs.cfg.LOGGER_FATAL_HEAD, error_msg, libs.cfg.LOGGER_FATAL_TAIL, sep="")
    print(libs.cfg.LOGGER_FATAL_HEAD)
    libs.cfg.logger.critical(
        "%s%s%s", libs.cfg.LOGGER_FATAL_HEAD, error_msg, libs.cfg.LOGGER_FATAL_TAIL
    )

    traceback.print_exc()

    libs.cfg.logger.debug(libs.cfg.LOGGER_END)

    sys.exit(1)
