# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
from typing import ClassVar

import sqlalchemy

class Document:
    DOCUMENT_DIRECTORY_TYPE_INBOX: ClassVar[str]
    DOCUMENT_DIRECTORY_TYPE_INBOX_ACCEPTED: ClassVar[str]
    DOCUMENT_DIRECTORY_TYPE_INBOX_REJECTED: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_FILE_DUPL: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_FILE_EXT: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_FILE_OPEN: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_NO_PDF_FORMAT: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_PARSER: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_PDF2IMAGE: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_TESSERACT: ClassVar[str]
    DOCUMENT_ERROR_CODE_REJ_TOKENIZE: ClassVar[str]
    DOCUMENT_STATUS_END: ClassVar[str]
    DOCUMENT_STATUS_ERROR: ClassVar[str]
    DOCUMENT_STATUS_START: ClassVar[str]

    def __init__(
        self,
        action_code_last: str,
        directory_name: str,
        file_name: str,
        id_language: int,
        id_run_last: int,
        _row_id: int = ...,
        action_text_last: str = ...,
        error_code_last: str = ...,
        error_msg_last: str = ...,
        error_no: int = ...,
        file_size_bytes: int = ...,
        no_lines_footer: int = ...,
        no_lines_header: int = ...,
        no_lines_toc: int = ...,
        no_lists_bullet: int = ...,
        no_lists_number: int = ...,
        no_tables: int = ...,
        no_pdf_pages: int = ...,
        sha256: str = ...,
        status: str = ...,
    ) -> None:
        self._exist = None
        self.document_action_code_last = None
        self.document_action_text_last = None
        self.document_directory_name = None
        self.document_error_code_last = None
        self.document_error_msg_last = None
        self.document_error_no = None
        self.document_file_name = None
        self.document_file_size_bytes = None
        self.document_id = None
        self.document_id_language = None
        self.document_id_run_last = None
        self.document_no_lines_footer = None
        self.document_no_lines_header = None
        self.document_no_lines_toc = None
        self.document_no_lists_bullet = None
        self.document_no_lists_number = None
        self.document_no_pdf_pages = None
        self.document_no_tables = None
        self.document_sha256 = None
        self.document_status = None
    def _get_columns(self) -> None: ...
    @classmethod
    def create_dbt(cls) -> None: ...
    def exists(self) -> bool: ...
    def finalise(self) -> None: ...
    def finalise_error(self, error_code: str, error_msg: str) -> None: ...
    @classmethod
    def from_id(cls, id_document: int) -> Document: ...
    @classmethod
    def from_row(cls, row: sqlalchemy.engine.Row) -> Document: ...
    def get_columns_in_tuple(self, is_file_size_bytes: bool = ..., is_sha256: bool = ...) -> tuple[int | str, ...]: ...
    def get_file_name_next(self) -> str: ...
    def get_file_type(self) -> str: ...
    def get_full_name(self) -> str: ...
    def get_stem_name(self) -> str: ...
    def get_stem_name_next(self) -> str: ...
    def persist_2_db(self) -> None: ...
    @classmethod
    def select_duplicate_file_name_by_sha256(cls, id_document: int, sha256: str) -> str: ...
