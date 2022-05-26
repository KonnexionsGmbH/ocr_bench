# pylint: disable=redefined-outer-name
"""Test Configuration and Fixtures.

Setup test config_setup.cfg.configurations and store fixtures.

Returns:
    [type]: None.
"""
import configparser
import os
import pathlib
import shutil
from typing import List
from typing import Tuple

import cfg.cls_setup
import cfg.glob
import db.cls_action
import db.cls_document
import db.cls_language
import db.cls_run
import db.cls_token
import db.cls_version
import db.driver
import pytest
import sqlalchemy
import utils

import dcr

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# pylint: disable=C0302
# pylint: disable=W0212
CONFIG_PARSER: configparser.ConfigParser = configparser.ConfigParser()

FILE_NAME_SETUP_CFG: str = "setup.cfg"
FILE_NAME_SETUP_CFG_BACKUP: str = "setup.cfg_backup"


# -----------------------------------------------------------------------------
# Backup and modify configuration parameter values.
# -----------------------------------------------------------------------------
# noinspection PyProtectedMember
@pytest.helpers.register
def backup_config_params(
    config_section: str,
    config_params: List[Tuple[str, str]],
) -> List[Tuple[str, str]]:
    """Backup and modify configuration parameter values.

    Args:
        config_section (str): Configuration section.
        config_params (List[Tuple[str, str]]): Configuration parameter modifications.

    Returns:
        List[Tuple[str, str]]: Original configuration parameter.
    """
    config_params_backup: List[Tuple[str, str]] = []

    CONFIG_PARSER.read(cfg.glob.setup._DCR_CFG_FILE)

    for (config_param, config_value) in config_params:
        config_params_backup.append((config_param, CONFIG_PARSER[config_section][config_param]))
        CONFIG_PARSER[config_section][config_param] = config_value

    with open(cfg.glob.setup._DCR_CFG_FILE, "w", encoding=cfg.glob.FILE_ENCODING_DEFAULT) as configfile:
        CONFIG_PARSER.write(configfile)

    return config_params_backup


# -----------------------------------------------------------------------------
# Backup the 'setup.cfg' file.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def backup_setup_cfg() -> None:
    """Backup the 'setup.cfg' file."""
    if not os.path.isfile(FILE_NAME_SETUP_CFG_BACKUP):
        shutil.copy2(FILE_NAME_SETUP_CFG, FILE_NAME_SETUP_CFG_BACKUP)


# -----------------------------------------------------------------------------
# Check the content of database table action.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def check_dbt_action(param: Tuple[int, Tuple[int, str, str, int, str, int, int, int]]) -> None:
    """Check the content of database table action.

    Args:
        param (Tuple[int, Tuple[int, str, str, int, str, int, int, int]]):
                Tuples with the contents of the table columns.
    """
    (id_row, expected_values) = param

    dbt = db.cls_action.Action.from_id(id_row)

    actual_values = dbt.get_columns_in_tuple(is_duration_ns=False, is_file_size_bytes=False)

    if expected_values != actual_values:
        print(f"issue with dbt action and id={id_row}:")
        print(f"values expected={expected_values}")
        print(f"values actual  ={actual_values}")
        assert False, f"issue with dbt action and id={id_row} - see above"


# -----------------------------------------------------------------------------
# Check the content of database table document.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def check_dbt_document(param: Tuple[int, Tuple[int, str, str, int, str, int, int, int]]) -> None:
    """Check the content of database table document.

    Args:
        param (Tuple[int, Tuple[int, str, str, int, str, int, int, int]]):
                Tuples with the contents of the table columns.
    """
    (id_row, expected_values) = param

    dbt = db.cls_document.Document.from_id(id_row)

    actual_values = dbt.get_columns_in_tuple(is_file_size_bytes=False)

    if expected_values != actual_values:
        print(f"issue with dbt document and id={id_row}:")
        print(f"values expected={expected_values}")
        print(f"values actual  ={actual_values}")
        assert False, f"issue with dbt document and id={id_row} - see above"


# -----------------------------------------------------------------------------
# Check the content of database table language.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def check_dbt_language(param: Tuple[int, Tuple[int, bool, str, str, str, str, str, str, str]]) -> None:
    """Check the content of database table language.

    Args:
        param (Tuple[int, Tuple[int, bool, str, str, str, str, str, str, str]]):
                Tuples with the contents of the table columns.
    """
    (id_row, expected_values) = param

    dbt = db.cls_language.Language.from_id(id_row)

    actual_values = dbt.get_columns_in_tuple()

    if expected_values != actual_values:
        print(f"issue with dbt language and id={id_row}:")
        print(f"values expected={expected_values}")
        print(f"values actual  ={actual_values}")
        assert False, f"issue with dbt language and id={id_row} - see above"


# -----------------------------------------------------------------------------
# Check the content of database table run.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def check_dbt_run(param: Tuple[int, Tuple[int, str, str, int, str, int, int, int]]) -> None:
    """Check the content of database table run.

    Args:
        param (Tuple[int, Tuple[int, str, str, int, str, int, int, int]]):
                Tuples with the contents of the table columns.
    """
    (id_row, expected_values) = param

    dbt = db.cls_run.Run.from_id(id_row)

    actual_values = dbt.get_columns_in_tuple()

    if expected_values != actual_values:
        print(f"issue with dbt run and id={id_row}:")
        print(f"values expected={expected_values}")
        print(f"values actual  ={actual_values}")
        assert False, f"issue with dbt run and id={id_row} - see above"


# -----------------------------------------------------------------------------
# Check the content of database table token.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def check_dbt_token(param: Tuple[int, Tuple[int, str, str, int, str, int, int, int]]) -> None:
    """Check the content of database table token.

    Args:
        param (Tuple[int, Tuple[int, str, str, int, str, int, int, int]]):
                Tuples with the contents of the table columns.
    """
    (id_row, expected_values) = param

    dbt = db.cls_token.Token.from_id(id_row)

    actual_values = dbt.get_columns_in_tuple()

    if expected_values != actual_values:
        print(f"issue with dbt token and id={id_row}:")
        print(f"values expected={expected_values}")
        print(f"values actual  ={actual_values}")
        assert False, f"issue with dbt token and id={id_row} - see above"


# -----------------------------------------------------------------------------
# Check the content of database table version.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def check_dbt_version(param: Tuple[int, Tuple[int, str]]) -> None:
    """Check the content of database table version.

    Args:
        param (Tuple[int, Tuple[int, str]]):
                Tuples with the contents of the table columns.
    """
    (id_row, expected_values) = param

    dbt = db.cls_version.Version.from_id(id_row)

    actual_values = dbt.get_columns_in_tuple()

    if expected_values != actual_values:
        print(f"issue with dbt version and id={id_row}:")
        print(f"values expected={expected_values}")
        print(f"values actual  ={actual_values}")
        assert False, f"issue with dbt version and id={id_row} - see above"


# -----------------------------------------------------------------------------
# Copy directories from the sample test file directory.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def copy_directories_4_pytest_2_dir(
    source_directories: List[str],
    target_dir: str,
) -> None:
    """Copy directories from the sample test file directory.

    Args:
        source_directories: List[str]: Source directory names.
        target_dir: str: Target directory.
    """
    assert os.path.isdir(utils.get_os_independent_name(cfg.glob.TESTS_INBOX_NAME)), (
        "source base directory '" + cfg.glob.TESTS_INBOX_NAME + "' missing"
    )

    for source in source_directories:
        source_dir = cfg.glob.TESTS_INBOX_NAME + "/" + source
        source_path = utils.get_full_name(cfg.glob.TESTS_INBOX_NAME, pathlib.Path(source))
        assert os.path.isdir(utils.get_os_independent_name(source_path)), (
            "source language directory '" + str(source_path) + "' missing"
        )
        target_path = utils.get_full_name(target_dir, pathlib.Path(source))
        shutil.copytree(source_dir, target_path)


# -----------------------------------------------------------------------------
# Copy files from the sample test file directory.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def copy_files_4_pytest(file_list: List[Tuple[Tuple[str, str | None], Tuple[pathlib.Path, List[str], str | None]]]) -> None:
    """Copy files from the sample test file directory.

    Args:
        file_list (List[
            Tuple[
                Tuple[str, str | None],
                Tuple[pathlib.Path, List[str], str | None]
            ]
        ]): List of files to be copied.
    """
    assert os.path.isdir(utils.get_os_independent_name(cfg.glob.TESTS_INBOX_NAME)), (
        "source directory '" + cfg.glob.TESTS_INBOX_NAME + "' missing"
    )

    for ((source_stem, source_ext), (target_dir, target_file_comp, target_ext)) in file_list:
        source_file_name = source_stem if source_ext is None else source_stem + "." + source_ext
        source_file = utils.get_full_name(cfg.glob.TESTS_INBOX_NAME, source_file_name)
        assert os.path.isfile(source_file), "source file '" + str(source_file) + "' missing"

        assert os.path.isdir(utils.get_os_independent_name(target_dir)), "target directory '" + target_dir + "' missing"
        target_file_name = (
            "_".join(target_file_comp) if target_ext is None else "_".join(target_file_comp) + "." + target_ext
        )
        target_file = utils.get_full_name(target_dir, target_file_name)
        assert os.path.isfile(target_file) is False, "target file '" + str(target_file) + "' already existing"

        shutil.copy(source_file, target_file)
        assert os.path.isfile(target_file), "target file '" + str(target_file) + "' is missing"


# -----------------------------------------------------------------------------
# Copy files from the sample test file directory.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def copy_files_4_pytest_2_dir(
    source_files: List[Tuple[str, str | None]],
    target_path: pathlib.Path,
) -> None:
    """Copy files from the sample test file directory.

    Args:
        source_files: List[Tuple[str, str | None]]: Source file names.
        target_path: Path: Target directory.
    """
    for source_file in source_files:
        (source_stem, source_ext) = source_file
        copy_files_4_pytest([(source_file, (target_path, [source_stem], source_ext))])


# -----------------------------------------------------------------------------
# Create one row in database table action.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def create_action():
    """Create one row in database table action.

    Returns:
        List: Column values
    """
    values = get_values_action()

    instance = db.cls_action.Action(
        action_code=values[1],
        action_text=values[2],
        directory_name=values[3],
        directory_type=values[4],
        file_name=values[8],
        file_size_bytes=values[9],
        id_document=values[10],
        id_parent=values[11],
        id_run_last=values[12],
        no_children=values[13],
        no_pdf_pages=values[14],
        status=values[15],
    )

    values[0] = instance.action_id

    return values


# -----------------------------------------------------------------------------
# Create one row in database table document.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def create_document():
    """Create one row in database table document.

    Returns:
        List: Column values
    """
    values = get_values_document()

    instance = db.cls_document.Document(
        action_code_last=values[1],
        directory_name=values[3],
        file_name=values[7],
        file_size_bytes=values[8],
        id_language=values[9],
        id_run_last=values[10],
        no_pdf_pages=values[11],
        sha256=values[12],
        status=values[13],
    )

    values[0] = instance.document_id

    return values


# -----------------------------------------------------------------------------
# Create one row in database table language.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def create_language():
    """Create one row in database table language.

    Returns:
        List: Column values
    """
    values = get_values_language()

    instance = db.cls_language.Language(
        active=values[1],
        code_iso_639_3=values[2],
        code_pandoc=values[3],
        code_spacy=values[4],
        code_tesseract=values[5],
        directory_name_inbox=values[6],
        iso_language_name=values[7],
    )

    instance.persist_2_db()

    values[0] = instance.language_id

    return values


# -----------------------------------------------------------------------------
# Create one row in database table run.
# -----------------------------------------------------------------------------
# noinspection PyArgumentList
@pytest.helpers.register
def create_run():
    """Create one row in database table run.

    Returns:
        List: Column values
    """
    values = get_values_run()

    instance = db.cls_run.Run(
        _row_id=0,
        action_code=values[1],
        status=values[4],
        total_erroneous=values[5],
    )

    instance.persist_2_db()

    values[0] = instance.run_id

    return values


# -----------------------------------------------------------------------------
# Create one row in database table token.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def create_token():
    """Create one row in database table token.

    Returns:
        List: Column values
    """
    values = get_values_token()

    instance = db.cls_token.Token(
        id_document=values[1],
        page_data=values[2],
        page_no=values[3],
    )

    values[0] = instance.token_id

    return values


# -----------------------------------------------------------------------------
# Create one row in database table version.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def create_version():
    """Create one row in database table version.

    Returns:
        List: Column values
    """
    values = get_values_version()

    instance = db.cls_version.Version(
        version=values[1],
    )

    instance.persist_2_db()

    values[0] = instance.version_id

    return values


# -----------------------------------------------------------------------------
# Delete the original configuration parameter value.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def delete_config_param(config_section: str, config_param: str) -> List[Tuple[str, str]]:
    """Delete the original configuration parameter value.

    Args:
        config_section (str): Configuration section.
        config_param (str): Configuration parameter.

    Returns:
        List[Tuple[str,str]]: Original configuration parameter.
    """
    CONFIG_PARSER.read(cfg.glob.setup._DCR_CFG_FILE)

    config_value_orig = CONFIG_PARSER[config_section][config_param]

    del CONFIG_PARSER[config_section][config_param]

    with open(cfg.glob.setup._DCR_CFG_FILE, "w", encoding=cfg.glob.FILE_ENCODING_DEFAULT) as configfile:
        CONFIG_PARSER.write(configfile)

    return [(config_param, config_value_orig)]


# -----------------------------------------------------------------------------
# Delete all entries in the database table 'version'.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def delete_version_version():
    """Delete all entries in the database table 'version'."""
    db.driver.connect_db()

    with cfg.glob.db_orm_engine.begin() as conn:
        version = sqlalchemy.Table(
            cfg.glob.DBT_VERSION,
            cfg.glob.db_orm_metadata,
            autoload_with=cfg.glob.db_orm_engine,
        )
        conn.execute(sqlalchemy.delete(version))

    db.driver.disconnect_db()


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


# -----------------------------------------------------------------------------
# Fixture - Setup empty database and empty inboxes.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_setup_empty_db_and_inbox(
    fxtr_mkdir,
    fxtr_rmdir_opt,
):
    """Fixture: Setup empty database and empty inboxes."""
    backup_setup_cfg()

    cfg.glob.setup = cfg.cls_setup.Setup()

    # restore original file
    shutil.copy(
        utils.get_full_name(cfg.glob.TESTS_INBOX_NAME, os.path.basename(pathlib.Path(cfg.glob.setup.initial_database_data))),
        os.path.dirname(pathlib.Path(cfg.glob.setup.initial_database_data)),
    )

    dcr.main([dcr.DCR_ARGV_0, db.cls_run.Run.ACTION_CODE_CREATE_DB])

    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox)
    fxtr_mkdir(cfg.glob.setup.directory_inbox)
    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_accepted)
    fxtr_mkdir(cfg.glob.setup.directory_inbox_accepted)
    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_rejected)
    fxtr_mkdir(cfg.glob.setup.directory_inbox_rejected)

    yield

    try:
        cfg.glob.setup.exists()  # type: ignore

        fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_rejected)
        fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_accepted)
        fxtr_rmdir_opt(cfg.glob.setup.directory_inbox)

        db.driver.drop_database()
    except AttributeError:
        pass

    restore_setup_cfg()


# -----------------------------------------------------------------------------
# Fixture - Setup empty database and empty inboxes.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_setup_empty_inbox(
    fxtr_mkdir,
    fxtr_rmdir_opt,
):
    """Fixture: Setup empty database and empty inboxes."""
    backup_setup_cfg()

    cfg.glob.setup = cfg.cls_setup.Setup()

    # restore original file
    shutil.copy(
        utils.get_full_name(cfg.glob.TESTS_INBOX_NAME, os.path.basename(pathlib.Path(cfg.glob.setup.initial_database_data))),
        os.path.dirname(pathlib.Path(cfg.glob.setup.initial_database_data)),
    )

    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox)
    fxtr_mkdir(cfg.glob.setup.directory_inbox)
    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_accepted)
    fxtr_mkdir(cfg.glob.setup.directory_inbox_accepted)
    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_rejected)
    fxtr_mkdir(cfg.glob.setup.directory_inbox_rejected)

    yield

    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_rejected)
    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox_accepted)
    fxtr_rmdir_opt(cfg.glob.setup.directory_inbox)

    db.driver.drop_database()

    restore_setup_cfg()


# -----------------------------------------------------------------------------
# Fixture - Setup logger.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_setup_logger():
    """Fixture: Setup logger & environment."""
    dcr.initialise_logger()

    yield


# -----------------------------------------------------------------------------
# Fixture - Setup logger & environment.
# -----------------------------------------------------------------------------
@pytest.fixture()
def fxtr_setup_logger_environment():
    """Fixture: Setup logger & environment."""
    cfg.glob.setup = cfg.cls_setup.Setup()

    # restore original file
    shutil.copy(
        utils.get_full_name(cfg.glob.TESTS_INBOX_NAME, os.path.basename(pathlib.Path(cfg.glob.setup.initial_database_data))),
        os.path.dirname(pathlib.Path(cfg.glob.setup.initial_database_data)),
    )

    cfg.glob.setup.environment_type = cfg.glob.setup.ENVIRONMENT_TYPE_TEST

    backup_setup_cfg()

    dcr.initialise_logger()

    yield

    restore_setup_cfg()


# -----------------------------------------------------------------------------
# Provide expected values - database table action.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_values_action():
    """Provide expected values - database table action."""
    return [
        None,
        "p_i",
        "inbox         (preprocessor)",
        cfg.glob.setup.directory_inbox,
        "inbox",
        "",
        "",
        0,
        "pdf_text_ok.pdf",
        53651,
        1,
        None,
        1,
        0,
        3,
        db.cls_document.Document.DOCUMENT_STATUS_START,
    ]


# -----------------------------------------------------------------------------
# Provide expected values - database table document.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_values_document():
    """Provide expected values - database table document."""
    return [
        None,
        "s_p_j_line",
        "parser_line   (nlp)",
        cfg.glob.setup.directory_inbox,
        "",
        "",
        0,
        "pdf_text_ok.pdf",
        53651,
        1,
        1,
        3,
        "e2402cc28e178911ee5941b1f9ac0d596beb7730f101da715f996dc992acbe25",
        db.cls_document.Document.DOCUMENT_STATUS_START,
    ]


# -----------------------------------------------------------------------------
# Provide expected values - database table language.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_values_language():
    """Provide expected values - database table language."""
    return [
        None,
        True,
        "xxx_code_iso_639_3",
        "xxx_code_pandoc",
        "xxx_code_spacy",
        "xxx_code_tesseract",
        "xxx_directory_name_inbox",
        "xxx_iso_language_name",
    ]


# -----------------------------------------------------------------------------
# Provide expected values - database table run.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_values_run():
    """Provide expected values - database table run."""
    return [
        None,
        "p_i",
        "inbox         (preprocessor)",
        1,
        db.cls_document.Document.DOCUMENT_STATUS_START,
        1,
        0,
        0,
    ]


# -----------------------------------------------------------------------------
# Provide expected values - database table token.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_values_token():
    """Provide expected values - database table token."""
    return [
        None,
        cfg.glob.document.document_id,
        {
            "pageNo": 1,
            "noTokensInPage": 221,
            "tokens": [
                {
                    "tknEntIob_": "O",
                    "tknI": 0,
                    "tknIsOov": True,
                    "tknIsSentStart": True,
                    "tknIsTitle": True,
                    "tknLemma_": "Start",
                    "tknNorm_": "start",
                    "tknPos_": "PROPN",
                    "tknTag_": "NNP",
                    "tknText": "Start",
                    "tknWhitespace_": " ",
                },
                {
                    "tknEntIob_": "O",
                    "tknI": 220,
                    "tknIsOov": True,
                    "tknIsPunct": True,
                    "tknIsSentEnd": True,
                    "tknLemma_": ".",
                    "tknNorm_": ".",
                    "tknPos_": "PUNCT",
                    "tknTag_": ".",
                    "tknText": ".",
                },
            ],
        },
        1,
    ]


# -----------------------------------------------------------------------------
# Provide expected values - database table version.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_values_version():
    """Provide expected values - database table version."""
    return [
        None,
        "xxx_version",
    ]


# -----------------------------------------------------------------------------
# Help RUN_ACTION_ALL_COMPLETE - duplicate file.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def help_run_action_all_complete_duplicate_file(
    file_ext_1: str, file_ext_2: str, stem_name_1: str, stem_name_2: str
) -> None:
    """Help RUN_ACTION_ALL_COMPLETE - duplicate file."""
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[(stem_name_1, file_ext_1)], target_path=cfg.glob.setup.directory_inbox_accepted
    )

    os.rename(
        utils.get_full_name(cfg.glob.setup.directory_inbox_accepted, stem_name_1 + "." + file_ext_1),
        utils.get_full_name(cfg.glob.setup.directory_inbox_accepted, stem_name_2 + "." + file_ext_2),
    )

    # -------------------------------------------------------------------------
    dcr.main([dcr.DCR_ARGV_0, db.cls_run.Run.ACTION_CODE_ALL_COMPLETE])

    # -------------------------------------------------------------------------
    verify_content_of_directory(
        cfg.glob.setup.directory_inbox,
        [],
        [],
    )

    verify_content_of_directory(
        cfg.glob.setup.directory_inbox_accepted,
        [],
        [stem_name_1 + "_1." + file_ext_1, stem_name_2 + "." + file_ext_2],
    )

    verify_content_of_directory(
        cfg.glob.setup.directory_inbox_rejected,
        [],
        [],
    )


# -----------------------------------------------------------------------------
# Help RUN_ACTION_PROCESS_INBOX - normal.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def help_run_action_process_inbox_normal(
    stem_name,
    file_ext,
):
    """Help RUN_ACTION_PROCESS_INBOX - normal."""
    pytest.helpers.copy_files_4_pytest_2_dir(
        source_files=[(stem_name, file_ext)], target_path=cfg.glob.setup.directory_inbox
    )

    # -------------------------------------------------------------------------
    dcr.main([dcr.DCR_ARGV_0, db.cls_run.Run.ACTION_CODE_INBOX])
    # -------------------------------------------------------------------------
    document_id: int = 1

    file_p_i = (
        cfg.glob.setup.directory_inbox_accepted,
        [stem_name, str(document_id)],
        file_ext,
    )

    verify_content_of_directory(
        cfg.glob.setup.directory_inbox,
        [],
        [],
    )

    verify_content_of_directory(
        cfg.glob.setup.directory_inbox_accepted,
        [],
        [stem_name + "_" + str(document_id) + "." + file_ext],
    )

    verify_content_of_directory(
        cfg.glob.setup.directory_inbox_rejected,
        [],
        [],
    )

    return document_id, file_p_i


# -----------------------------------------------------------------------------
# Insert a new configuration parameter.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def insert_config_param(
    config_section: str,
    config_param: str,
    config_value_new: str,
) -> None:
    """Insert a new configuration parameter.

    Args:
        config_section (str): Configuration section.
        config_param (str): Configuration parameter.
        config_value_new (str): New configuration parameter value.
    """
    CONFIG_PARSER.read(cfg.glob.setup._DCR_CFG_FILE)

    CONFIG_PARSER[config_section][config_param] = config_value_new

    with open(cfg.glob.setup._DCR_CFG_FILE, "w", encoding=cfg.glob.FILE_ENCODING_DEFAULT) as configfile:
        CONFIG_PARSER.write(configfile)


# -----------------------------------------------------------------------------
# Restore the original configuration parameter.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def restore_config_params(
    config_section: str,
    config_params: List[Tuple[str, str]],
) -> None:
    """Restore the original configuration parameter.

    Args:
        config_section (str): Configuration section.
        config_params (List[Tuple[str, str]]): Configuration parameter modifications.
    """
    for (config_param, config_value) in config_params:
        CONFIG_PARSER[config_section][config_param] = config_value

    with open(cfg.glob.setup._DCR_CFG_FILE, "w", encoding=cfg.glob.FILE_ENCODING_DEFAULT) as configfile:
        CONFIG_PARSER.write(configfile)

    cfg.glob.setup = cfg.cls_setup.Setup()


# -----------------------------------------------------------------------------
# Restore the 'setup.cfg' file.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def restore_setup_cfg():
    """Restore the 'setup.cfg' file."""
    shutil.copy2(FILE_NAME_SETUP_CFG_BACKUP, FILE_NAME_SETUP_CFG)

    os.remove(FILE_NAME_SETUP_CFG_BACKUP)


# -----------------------------------------------------------------------------
# Set all SpaCy configuration parameters to the same logical value.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def set_complete_cfg_spacy(false_or_true: str):
    """Set all SpaCy configuration parameters to the same logical value."""
    return pytest.helpers.backup_config_params(
        cfg.glob.setup._DCR_CFG_SECTION_SPACY,
        [
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_DEP_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_DOC, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_HEAD, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_I, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IDX, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LANG_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LEX, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_MORPH, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_NORM_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_POS_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_PROB, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_RANK, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_SENT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_TAG_, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_TEXT, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB, false_or_true),
            (cfg.glob.setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_, false_or_true),
        ],
    )


# -----------------------------------------------------------------------------
# Run before all tests.
# -----------------------------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def setup_dcr():
    """Run before all tests."""
    dcr.initialise_logger()


# -----------------------------------------------------------------------------
# Store and modify the original configuration parameter value.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def store_config_param(
    config_section: str,
    config_param: str,
    config_value_new: str,
) -> str:
    """Store and modify the original configuration parameter value.

    Args:
        config_section (str): Configuration section.
        config_param (str): Configuration parameter.
        config_value_new (str): New configuration parameter value.

    Returns:
        str: Original configuration parameter value.
    """
    CONFIG_PARSER.read(cfg.glob.setup._DCR_CFG_FILE)

    config_value_orig = CONFIG_PARSER[config_section][config_param]

    CONFIG_PARSER[config_section][config_param] = config_value_new

    with open(cfg.glob.setup._DCR_CFG_FILE, "w", encoding=cfg.glob.FILE_ENCODING_DEFAULT) as configfile:
        CONFIG_PARSER.write(configfile)

    return config_value_orig


# -----------------------------------------------------------------------------
# Verify the content of a file directory.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def verify_content_of_directory(
    directory_name: str,
    expected_directories: List[str],
    expected_files: List[str],
) -> None:
    """Verify the content of a file directory.

    Args:
        directory_name: str:
                   Name of the file directory to be checked.
        expected_directories: List[str]:
                   List of the expected directory names.
        expected_files: List[str]:
                   List of the expected file names.
    """
    cfg.glob.logger.info("directory name   =%s", directory_name)

    directory_content = os.listdir(directory_name)
    cfg.glob.logger.info("existing directory content=%s", str(directory_content))
    cfg.glob.logger.info("expected directory content=%s", str(expected_directories))
    cfg.glob.logger.info("expected file      content=%s", str(expected_files))

    # check directory content against expectations
    for elem in directory_content:
        elem_path = utils.get_full_name(directory_name, elem)
        if os.path.isdir(elem_path):
            assert elem in expected_directories, f"directory {elem} was not expected"
        else:
            assert elem in expected_files, f"file {elem} was not expected"

    # check expected directories against directory content
    for elem in expected_directories:
        assert elem in directory_content, f"expected directory {elem} is missing"
        elem_path = utils.get_full_name(directory_name, elem)
        assert os.path.isdir(utils.get_os_independent_name(elem_path)), f"expected directory {elem} is a file"

    # check expected files against directory content
    for elem in expected_files:
        assert elem in directory_content, f"expected file {elem} is missing"
        elem_path = utils.get_full_name(directory_name, elem)
        assert os.path.isfile(elem_path), f"expected file {elem} is a directory"


# -----------------------------------------------------------------------------
# Verify the content of an inbox directories.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def verify_content_of_inboxes(
    inbox: Tuple[List[str], List[str]] = ([], []),
    inbox_accepted: Tuple[List[str], List[str]] = ([], []),
    inbox_rejected: Tuple[List[str], List[str]] = ([], []),
) -> None:
    """Verify the content of an inbox directories..

    Args:
        inbox: Tuple[List[str],List[str]]:
                   An optional list of expected directories and
                   an optional list of expected files in the inbox directory.
        inbox_accepted: Tuple[List[str],List[str]]:
                   An optional list of expected directories and
                   an optional list of expected files in the inbox_accepted directory.
        inbox_rejected: Tuple[List[str],List[str]]:
                   An optional list of expected directories and
                   an optional list of expected files in the inbox_rejected directory.
    """
    verify_content_of_directory(
        directory_name=cfg.glob.setup.directory_inbox,
        expected_directories=inbox[0],
        expected_files=inbox[1],
    )

    verify_content_of_directory(
        directory_name=cfg.glob.setup.directory_inbox_accepted,
        expected_directories=inbox_accepted[0],
        expected_files=inbox_accepted[1],
    )
    verify_content_of_directory(
        directory_name=cfg.glob.setup.directory_inbox_rejected,
        expected_directories=inbox_rejected[0],
        expected_files=inbox_rejected[1],
    )
