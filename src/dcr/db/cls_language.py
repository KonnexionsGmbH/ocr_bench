# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module dcr.db.cls_language: Managing the database table language."""
from __future__ import annotations

import os.path
from typing import ClassVar

import dcr_core.core_glob
import dcr_core.core_utils
import sqlalchemy
import sqlalchemy.engine
import sqlalchemy.orm

import dcr.cfg.glob
import dcr.db.cls_db_core
import dcr.utils


# pylint: disable=duplicate-code
# pylint: disable=too-many-instance-attributes
class Language:
    """Managing the database table language.

    Returns:
        _type_: Language instance.
    """

    # -----------------------------------------------------------------------------
    # Class variables.
    # -----------------------------------------------------------------------------
    LANGUAGES_PANDOC: ClassVar[dict[int, str]]
    LANGUAGES_SPACY: ClassVar[dict[int, str]]
    LANGUAGES_TESSERACT: ClassVar[dict[int, str]]

    # -----------------------------------------------------------------------------
    # Initialise the instance.
    # -----------------------------------------------------------------------------
    def __init__(
        self,
        code_iso_639_3: str,
        code_pandoc: str,
        code_spacy: str,
        code_tesseract: str,
        iso_language_name: str,
        _row_id: int = 0,
        active: bool = False,
        directory_name_inbox: str = "",
    ) -> None:
        """Initialise the instance.

        Args:
            code_iso_639_3 (str):
                    The ISO 639-3 code of the language.
            code_pandoc (str):
                    The Pandoc code of the language.
            code_spacy (str):
                    The spaCy code of the model to be applied.
            code_tesseract (str):
                    The Tesseract OCR code of the language.
            iso_language_name (str):
                    The English name of the language.
            _row_id (int, optional):
                    Row id. Defaults to 0.
            active (bool, optional):
                    Is the language active?. Defaults to False.
            directory_name_inbox (str, optional):
                    Name of the language-specific input file directory. Defaults to "".
        """
        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

        dcr.utils.check_exists_object(
            is_db_core=True,
        )
        dcr_core.core_utils.check_exists_object(
            is_setup=True,
        )

        self.language_active = active
        self.language_code_iso_639_3 = code_iso_639_3
        self.language_code_pandoc = code_pandoc
        self.language_code_spacy = code_spacy
        self.language_code_tesseract = code_tesseract

        if self.language_active and (directory_name_inbox is None or directory_name_inbox == ""):
            self.language_directory_name_inbox = str(os.path.join(dcr_core.core_glob.setup.directory_inbox, iso_language_name.lower()))
        else:
            self.language_directory_name_inbox = dcr_core.core_utils.get_os_independent_name(directory_name_inbox)

        self.language_id = _row_id
        self.language_iso_language_name = iso_language_name

        self.total_erroneous = 0
        self.total_processed = 0
        self.total_processed_to_be = 0
        self.total_processed_pandoc = 0
        self.total_processed_pdf2image = 0
        self.total_processed_pdflib = 0
        self.total_processed_tesseract = 0

        self._exist = True

        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

    # -----------------------------------------------------------------------------
    # Get the database columns.
    # -----------------------------------------------------------------------------
    def _get_columns(self) -> dcr.db.cls_db_core.Columns:
        """Get the database columns.

        Returns:
            dcr.db.cls_db_core.Columns:
                    Database columns.
        """
        return {
            dcr.db.cls_db_core.DBCore.DBC_ACTIVE: self.language_active,
            dcr.db.cls_db_core.DBCore.DBC_CODE_ISO_639_3: self.language_code_iso_639_3,
            dcr.db.cls_db_core.DBCore.DBC_CODE_PANDOC: self.language_code_pandoc,
            dcr.db.cls_db_core.DBCore.DBC_CODE_SPACY: self.language_code_spacy,
            dcr.db.cls_db_core.DBCore.DBC_CODE_TESSERACT: self.language_code_tesseract,
            dcr.db.cls_db_core.DBCore.DBC_DIRECTORY_NAME_INBOX: self.language_directory_name_inbox,
            dcr.db.cls_db_core.DBCore.DBC_ISO_LANGUAGE_NAME: self.language_iso_language_name,
        }

    # -----------------------------------------------------------------------------
    # Create the database table.
    # -----------------------------------------------------------------------------
    @classmethod
    def create_dbt(cls) -> None:
        """Create the database table."""
        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

        sqlalchemy.Table(
            dcr.db.cls_db_core.DBCore.DBT_LANGUAGE,
            dcr.cfg.glob.db_core.db_orm_metadata,
            sqlalchemy.Column(
                dcr.db.cls_db_core.DBCore.DBC_ID,
                sqlalchemy.Integer,
                autoincrement=True,
                nullable=False,
                primary_key=True,
            ),
            sqlalchemy.Column(
                dcr.db.cls_db_core.DBCore.DBC_CREATED_AT,
                sqlalchemy.DateTime,
            ),
            sqlalchemy.Column(
                dcr.db.cls_db_core.DBCore.DBC_MODIFIED_AT,
                sqlalchemy.DateTime,
            ),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_ACTIVE, sqlalchemy.Boolean, default=True, nullable=False),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_CODE_ISO_639_3, sqlalchemy.String, nullable=False, unique=True),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_CODE_PANDOC, sqlalchemy.String, nullable=False, unique=True),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_CODE_SPACY, sqlalchemy.String, nullable=False, unique=True),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_CODE_TESSERACT, sqlalchemy.String, nullable=False, unique=True),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_DIRECTORY_NAME_INBOX, sqlalchemy.String, nullable=True, unique=True),
            sqlalchemy.Column(dcr.db.cls_db_core.DBCore.DBC_ISO_LANGUAGE_NAME, sqlalchemy.String, nullable=False, unique=True),
        )

        dcr.utils.progress_msg(f"The database table '{dcr.db.cls_db_core.DBCore.DBT_LANGUAGE}' has now been created")

        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

    # -----------------------------------------------------------------------------
    # Check the object existence.
    # -----------------------------------------------------------------------------
    def exists(self) -> bool:
        """Check the object existence.

        Returns:
            bool:   Always true
        """
        return self._exist

    # -----------------------------------------------------------------------------
    # Initialise from id.
    # -----------------------------------------------------------------------------
    @classmethod
    def from_id(cls, id_language: int) -> Language:
        """Initialise from row id.

        Args:
            id_language (int):
                    The required row id.

        Returns:
            Language:
                    The object instance found.
        """
        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)
        # dcr_core.core_glob.logger.debug("param id_language=%i", id_language)

        dbt = sqlalchemy.Table(
            dcr.db.cls_db_core.DBCore.DBT_LANGUAGE,
            dcr.cfg.glob.db_core.db_orm_metadata,
            autoload_with=dcr.cfg.glob.db_core.db_orm_engine,
        )

        with dcr.cfg.glob.db_core.db_orm_engine.connect() as conn:
            row = conn.execute(
                sqlalchemy.select(dbt).where(
                    dbt.c.id == id_language,
                )
            ).fetchone()
            conn.close()

        if row is None:
            dcr_core.core_utils.terminate_fatal(
                f"The language with id={id_language} does not exist in the database table 'language'",
            )

        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

        return Language.from_row(row)  # type: ignore

    # -----------------------------------------------------------------------------
    # Initialise from a database row.
    # -----------------------------------------------------------------------------
    @classmethod
    def from_row(cls, row: sqlalchemy.engine.Row) -> Language:
        """Initialise from a database row.

        Args:
            row (sqlalchemy.engine.Row):
                    A appropriate database row.

        Returns:
            Language:
                    The object instance matching the specified database row.
        """
        return cls(
            _row_id=row[dcr.db.cls_db_core.DBCore.DBC_ID],
            active=row[dcr.db.cls_db_core.DBCore.DBC_ACTIVE],
            code_iso_639_3=row[dcr.db.cls_db_core.DBCore.DBC_CODE_ISO_639_3],
            code_pandoc=row[dcr.db.cls_db_core.DBCore.DBC_CODE_PANDOC],
            code_spacy=row[dcr.db.cls_db_core.DBCore.DBC_CODE_SPACY],
            code_tesseract=row[dcr.db.cls_db_core.DBCore.DBC_CODE_TESSERACT],
            directory_name_inbox=row[dcr.db.cls_db_core.DBCore.DBC_DIRECTORY_NAME_INBOX],
            iso_language_name=row[dcr.db.cls_db_core.DBCore.DBC_ISO_LANGUAGE_NAME],
        )

    # -----------------------------------------------------------------------------
    # Get the database columns in a tuple.
    # -----------------------------------------------------------------------------
    def get_columns_in_tuple(
        self,
    ) -> tuple[int, bool, str, str, str, str, str, str]:
        """Get the database columns in a tuple.

        Returns:
            tuple[int, bool, str, str, str, str, str, str]:
                    Column values in a tuple.
        """
        return (
            self.language_id,
            self.language_active,
            self.language_code_iso_639_3,
            self.language_code_pandoc,
            self.language_code_spacy,
            self.language_code_tesseract,
            self.language_directory_name_inbox,
            self.language_iso_language_name,
        )

    # -----------------------------------------------------------------------------
    # Load the data from the database table 'language'.
    # -----------------------------------------------------------------------------
    @classmethod
    def load_data_from_dbt_language(cls) -> None:
        """Load the data from the database table 'language'."""
        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

        dbt = sqlalchemy.Table(
            dcr.db.cls_db_core.DBCore.DBT_LANGUAGE,
            dcr.cfg.glob.db_core.db_orm_metadata,
            autoload_with=dcr.cfg.glob.db_core.db_orm_engine,
        )

        Language.LANGUAGES_PANDOC = {}
        Language.LANGUAGES_SPACY = {}
        Language.LANGUAGES_TESSERACT = {}

        with dcr.cfg.glob.db_core.db_orm_engine.connect() as conn:
            rows = conn.execute(
                sqlalchemy.select(dbt.c.id, dbt.c.code_pandoc, dbt.c.code_spacy, dbt.c.code_tesseract).where(
                    dbt.c.active,
                )
            )

            for row in rows:
                Language.LANGUAGES_PANDOC[row.id] = row.code_pandoc
                Language.LANGUAGES_SPACY[row.id] = row.code_spacy
                Language.LANGUAGES_TESSERACT[row.id] = row.code_tesseract

            conn.close()

        dcr.utils.progress_msg(f"Available languages for Pandoc        '{Language.LANGUAGES_PANDOC}'")
        dcr.utils.progress_msg(f"Available languages for spaCy         '{Language.LANGUAGES_SPACY}'")
        dcr.utils.progress_msg(f"Available languages for Tesseract OCR '{Language.LANGUAGES_TESSERACT}'")

        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

    # -----------------------------------------------------------------------------
    # Persist the object in the database.
    # -----------------------------------------------------------------------------
    def persist_2_db(self) -> None:
        """Persist the object in the database."""
        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

        if self.language_id == 0:
            self.language_id = dcr.cfg.glob.db_core.insert_dbt_row(  # type: ignore
                dcr.db.cls_db_core.DBCore.DBT_LANGUAGE,  # type: ignore
                self._get_columns(),  # type: ignore
            )
        else:
            dcr.cfg.glob.db_core.update_dbt_id(  # type: ignore
                table_name=dcr.db.cls_db_core.DBCore.DBT_LANGUAGE,
                id_where=self.language_id,
                columns=self._get_columns(),
            )

        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

    # -----------------------------------------------------------------------------
    # Get the active languages.
    # -----------------------------------------------------------------------------
    @classmethod
    def select_active_languages(cls, conn: sqlalchemy.engine.Connection) -> sqlalchemy.engine.CursorResult:
        """Get the languages to be processed.

        Args:
            conn (Connection):
                    Database connection.

        Returns:
            engine.CursorResult:
                    The languages found.
        """
        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_START)

        dbt = sqlalchemy.Table(
            dcr.db.cls_db_core.DBCore.DBT_LANGUAGE,
            dcr.cfg.glob.db_core.db_orm_metadata,
            autoload_with=dcr.cfg.glob.db_core.db_orm_engine,
        )

        # dcr_core.core_glob.logger.debug(dcr_core.core_glob.LOGGER_END)

        return conn.execute(
            sqlalchemy.select(dbt)
            .where(
                dbt.c.active,
            )
            .order_by(dbt.c.id.asc())
        )
