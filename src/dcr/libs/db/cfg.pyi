"""Library Stub."""
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
DBC_ACTIVE: str
DBC_CHILD_NO: str
DBC_CODE_ISO_639_3: str
DBC_CODE_SPACY: str
DBC_CODE_TESSERACT: str
DBC_CREATED_AT: str
DBC_DIRECTORY_NAME: str
DBC_DIRECTORY_NAME_INBOX: str
DBC_DIRECTORY_TYPE: str
DBC_DOCUMENT_ID: str
DBC_DOCUMENT_ID_BASE: str
DBC_DOCUMENT_ID_PARENT: str
DBC_DURATION_NS: str
DBC_ERROR_CODE: str
DBC_ERROR_TEXT: str
DBC_FILE_NAME: str
DBC_FILE_TYPE: str
DBC_FUNCTION_NAME: str
DBC_ID: str
DBC_ISO_LANGUAGE_NAME: str
DBC_LANGUAGE_ID: str
DBC_LINE_IN_PARA: str
DBC_MODIFIED_AT: str
DBC_MODULE_NAME: str
DBC_NEXT_STEP: str
DBC_PAGE_IN_DOCUMENT: str
DBC_PARA_IN_PAGE: str
DBC_RUN_ID: str
DBC_SENTENCE_IN_PARA: str
DBC_SHA256: str
DBC_STATUS: str
DBC_STEM_NAME: str
DBC_TOKEN_IN_LINE: str
DBC_TOKEN_IN_SENTENCE: str
DBC_TOKEN_LEMMA: str
DBC_TOKEN_PARSED: str
DBC_TOKEN_STEM: str
DBC_TOTAL_ERRONEOUS: str
DBC_TOTAL_OK_PROCESSED: str
DBC_TOTAL_TO_BE_PROCESSED: str
DBC_VERSION: str

DBT_CONTENT: str
DBT_DOCUMENT: str
DBT_JOURNAL: str
DBT_LANGUAGE: str
DBT_RUN: str
DBT_VERSION: str

DOCUMENT_DIRECTORY_TYPE_INBOX: str
DOCUMENT_DIRECTORY_TYPE_INBOX_ACCEPTED: str
DOCUMENT_DIRECTORY_TYPE_INBOX_REJECTED: str

DOCUMENT_ERROR_CODE_REJ_ERROR: str
DOCUMENT_ERROR_CODE_REJ_FILE_DUPL: str
DOCUMENT_ERROR_CODE_REJ_FILE_ERROR: str
DOCUMENT_ERROR_CODE_REJ_FILE_EXT: str
DOCUMENT_ERROR_CODE_REJ_FILE_MOVE: str
DOCUMENT_ERROR_CODE_REJ_FILE_RIGHTS: str
DOCUMENT_ERROR_CODE_REJ_NO_PDF_FORMAT: str
DOCUMENT_ERROR_CODE_REJ_PANDOC: str
DOCUMENT_ERROR_CODE_REJ_PARSER: str
DOCUMENT_ERROR_CODE_REJ_PDF2IMAGE: str
DOCUMENT_ERROR_CODE_REJ_PDFLIB: str
DOCUMENT_ERROR_CODE_REJ_TESSERACT: str

DOCUMENT_FILE_TYPE_JPG: str
DOCUMENT_FILE_TYPE_PANDOC: List[str]
DOCUMENT_FILE_TYPE_PDF: str
DOCUMENT_FILE_TYPE_PNG: str
DOCUMENT_FILE_TYPE_TESSERACT: List[str]
DOCUMENT_FILE_TYPE_TIF: str
DOCUMENT_FILE_TYPE_TIFF: str
DOCUMENT_FILE_TYPE_XML: str

DOCUMENT_NEXT_STEP_PANDOC: str
DOCUMENT_NEXT_STEP_PARSER: str
DOCUMENT_NEXT_STEP_PDF2IMAGE: str
DOCUMENT_NEXT_STEP_PDFLIB: str
DOCUMENT_NEXT_STEP_TESSERACT: str

DOCUMENT_STATUS_ABORT: str
DOCUMENT_STATUS_END: str
DOCUMENT_STATUS_ERROR: str
DOCUMENT_STATUS_START: str

JSON_NAME_API_VERSION: str
JSON_NAME_COLUMN_NAME: str
JSON_NAME_COLUMN_VALUE: str
JSON_NAME_DATA: str
JSON_NAME_ROW: str
JSON_NAME_ROWS: str
JSON_NAME_TABLES: str
JSON_NAME_TABLE_NAME: str

JOURNAL_ACTION_01_901: str
JOURNAL_ACTION_01_902: str
JOURNAL_ACTION_01_903: str
JOURNAL_ACTION_01_904: str
JOURNAL_ACTION_01_905: str
JOURNAL_ACTION_01_906: str

JOURNAL_ACTION_21_901: str
JOURNAL_ACTION_21_902: str
JOURNAL_ACTION_21_903: str

JOURNAL_ACTION_31_901: str
JOURNAL_ACTION_31_902: str
JOURNAL_ACTION_31_903: str

JOURNAL_ACTION_41_901: str
JOURNAL_ACTION_41_902: str
JOURNAL_ACTION_41_903: str

JOURNAL_ACTION_51_901: str
JOURNAL_ACTION_51_902: str
JOURNAL_ACTION_51_903: str

JOURNAL_ACTION_61_901: str
JOURNAL_ACTION_61_902: str
JOURNAL_ACTION_61_903: str

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
