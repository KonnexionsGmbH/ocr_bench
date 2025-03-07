# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
from typing import ClassVar

import sqlalchemy.orm
from sqlalchemy import Integer
from sqlalchemy import String

class Run:
    _ACTION_TEXT_INBOX = None
    _ACTION_TEXT_PANDOC = None
    _ACTION_TEXT_PARSER = None
    _ACTION_TEXT_PARSER_LINE = None
    _ACTION_TEXT_PARSER_PAGE = None
    _ACTION_TEXT_PARSER_WORD = None
    _ACTION_TEXT_PDF2IMAGE = None
    _ACTION_TEXT_PDFLIB = None
    _ACTION_TEXT_TESSERACT = None
    _ACTION_TEXT_TOKENIZE = None
    _ACTION_TEXT_TOKENIZE_LINE = None
    ACTION_CODE_ALL_COMPLETE: ClassVar[str]
    ACTION_CODE_CREATE_DB: ClassVar[str]
    ACTION_CODE_EXPORT_LT_RULES: ClassVar[str]
    ACTION_CODE_INBOX: ClassVar[str]
    ACTION_CODE_PANDOC: ClassVar[str]
    ACTION_CODE_PARSER: ClassVar[str]
    ACTION_CODE_PARSER_LINE: ClassVar[str]
    ACTION_CODE_PARSER_PAGE: ClassVar[str]
    ACTION_CODE_PARSER_WORD: ClassVar[str]
    ACTION_CODE_PDF2IMAGE: ClassVar[str]
    ACTION_CODE_PDFLIB: ClassVar[str]
    ACTION_CODE_PYPDF2: ClassVar[str]
    ACTION_CODE_TESSERACT: ClassVar[str]
    ACTION_CODE_TOKENIZE: ClassVar[str]
    ACTION_CODE_TOKENIZE_LINE: ClassVar[str]
    ACTION_CODE_UPGRADE_DB: ClassVar[str]
    ID_RUN_UMBRELLA: ClassVar[int]

    def __init__(
        self,
        action_code: str,
        _row_id: int = ...,
        action_text: str = ...,
        id_run: int = ...,
        status: str = ...,
        total_erroneous: int = ...,
        total_processed_ok: int = ...,
        total_processed_to_be: int = ...,
    ) -> None:
        self._exist = None
        self.run_action_code = None
        self.run_action_text = None
        self.run_id = None
        self.run_id_run = None
        self.run_status = None
        self.run_total_erroneous = None
        self.run_total_processed_ok = None
        self.run_total_processed_to_be = None
        self.total_generated = None
        self.total_processed_pandoc = None
        self.total_processed_pdf2image = None
        self.total_processed_pdflib = None
        self.total_processed_tesseract = None
        self.total_status_error = None
        self.total_status_ready = None
    def _get_columns(self) -> None: ...
    @classmethod
    def create_dbt(cls) -> None: ...
    def exists(self) -> bool: ...
    def finalise(self) -> None: ...
    @classmethod
    def from_id(cls, id_run: int) -> Run: ...
    @classmethod
    def from_row(cls, row: sqlalchemy.engine.Row) -> Run: ...
    @classmethod
    def get_action_text(cls, action_code: str) -> str: ...
    def get_columns_in_tuple(
        self,
    ) -> tuple[int | Integer, str, str, int | Integer, str | String, int | Integer, int | Integer, int | Integer,]: ...
    @classmethod
    def get_id_latest(cls) -> int: ...
    def persist_2_db(self) -> None: ...
