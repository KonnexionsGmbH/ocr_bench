"""Library Stub.

Returns:
    [type]: None.
"""
from typing import List

from psycopg2.extensions import connection
from psycopg2.extensions import cursor
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine

# -----------------------------------------------------------------------------
# Global Constants.
# -----------------------------------------------------------------------------
DB_DIALECT_POSTGRESQL: str

DBC_ACTION: str
DBC_ACTION_CODE: str
DBC_ACTION_TEXT: str
DBC_CHILD_NO: str
DBC_CREATED_AT: str
DBC_DIRECTORY_NAME: str
DBC_DIRECTORY_TYPE: str
DBC_DOCUMENT_ID: str
DBC_DOCUMENT_ID_BASE: str
DBC_DOCUMENT_ID_PARENT: str
DBC_ERROR_CODE: str
DBC_FILE_NAME: str
DBC_FILE_TYPE: str
DBC_FUNCTION_NAME: str
DBC_ID: str
DBC_MODIFIED_AT: str
DBC_MODULE_NAME: str
DBC_NEXT_STEP: str
DBC_RUN_ID: str
DBC_SHA256: str
DBC_STATUS: str
DBC_STEM_NAME: str
DBC_TOTAL_ERRONEOUS: str
DBC_TOTAL_OK_PROCESSED: str
DBC_TOTAL_TO_BE_PROCESSED: str
DBC_VERSION: str

DBT_DOCUMENT: str
DBT_JOURNAL: str
DBT_RUN: str
DBT_VERSION: str

DOCUMENT_DIRECTORY_TYPE_INBOX: str
DOCUMENT_DIRECTORY_TYPE_INBOX_ACCEPTED: str
DOCUMENT_DIRECTORY_TYPE_INBOX_REJECTED: str

DOCUMENT_ERROR_CODE_REJECTED_ERROR: str
DOCUMENT_ERROR_CODE_REJECTED_FILE_DUPL: str
DOCUMENT_ERROR_CODE_REJECTED_FILE_ERROR: str
DOCUMENT_ERROR_CODE_REJECTED_FILE_EXT: str
DOCUMENT_ERROR_CODE_REJECTED_FILE_MOVE: str
DOCUMENT_ERROR_CODE_REJECTED_FILE_RIGHTS: str
DOCUMENT_ERROR_CODE_REJECTED_NO_PDF_FORMAT: str
DOCUMENT_ERROR_CODE_REJECTED_PDF2IMAGE: str

DOCUMENT_FILE_TYPE_JPG: str
DOCUMENT_FILE_TYPE_PANDOC: List[str]
DOCUMENT_FILE_TYPE_PDF: str
DOCUMENT_FILE_TYPE_PNG: str
DOCUMENT_FILE_TYPE_TESSERACT: List[str]

DOCUMENT_NEXT_STEP_PANDOC: str
DOCUMENT_NEXT_STEP_PDF2IMAGE: str
DOCUMENT_NEXT_STEP_PDFLIB: str
DOCUMENT_NEXT_STEP_TESSERACT: str

DOCUMENT_STATUS_ABORT: str
DOCUMENT_STATUS_END: str
DOCUMENT_STATUS_ERROR: str
DOCUMENT_STATUS_START: str

JOURNAL_ACTION_01_001: str
JOURNAL_ACTION_01_002: str
JOURNAL_ACTION_01_003: str
JOURNAL_ACTION_01_901: str
JOURNAL_ACTION_01_902: str
JOURNAL_ACTION_01_903: str
JOURNAL_ACTION_01_904: str
JOURNAL_ACTION_01_905: str
JOURNAL_ACTION_11_001: str
JOURNAL_ACTION_11_002: str
JOURNAL_ACTION_11_003: str
JOURNAL_ACTION_21_001: str
JOURNAL_ACTION_21_002: str
JOURNAL_ACTION_21_003: str
JOURNAL_ACTION_21_901: str
JOURNAL_ACTION_21_902: str

RUN_STATUS_END: str
RUN_STATUS_START: str

# -----------------------------------------------------------------------------
# Global Constants.
# -----------------------------------------------------------------------------

db_current_database: str
db_current_user: str
db_driver_conn: connection | None = None
db_driver_cur: cursor | None = None
db_orm_engine: Engine | None = None
db_orm_metadata: MetaData | None = None
