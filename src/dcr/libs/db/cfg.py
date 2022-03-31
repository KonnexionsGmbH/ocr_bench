"""Module libs.db.cfg: Database Configuration Data."""
from typing import List

from psycopg2.extensions import connection
from psycopg2.extensions import cursor
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine

# -----------------------------------------------------------------------------
# Global Constants.
# -----------------------------------------------------------------------------
DB_DIALECT_POSTGRESQL: str = "postgresql"

DBC_ACTION: str = "action"
DBC_ACTIVE: str = "active"
DBC_CHILD_NO: str = "child_no"
DBC_CODE_ISO_639_3: str = "code_iso_639_3"
DBC_CODE_SPACY: str = "code_spacy"
DBC_CODE_TESSERACT: str = "code_tesseract"
DBC_CREATED_AT: str = "created_at"
DBC_DIRECTORY_NAME: str = "directory_name"
DBC_DIRECTORY_NAME_INBOX: str = "directory_name_inbox"
DBC_DIRECTORY_TYPE: str = "directory_type"
DBC_DOCUMENT_ID: str = "document_id"
DBC_DOCUMENT_ID_BASE: str = "document_id_base"
DBC_DOCUMENT_ID_PARENT: str = "document_id_parent"
DBC_DURATION_NS: str = "duration_ns"
DBC_ERROR_CODE: str = "error_code"
DBC_ERROR_TEXT: str = "error_text"
DBC_FILE_NAME: str = "file_name"
DBC_FILE_TYPE: str = "file_type"
DBC_FUNCTION_NAME: str = "function_name"
DBC_ID: str = "id"
DBC_ISO_LANGUAGE_NAME: str = "iso_language_name"
DBC_LANGUAGE_ID: str = "language_id"
DBC_LINE_IN_PARA: str = "line_in_para"
DBC_MODIFIED_AT: str = "modified_at"
DBC_MODULE_NAME: str = "module_name"
DBC_NEXT_STEP: str = "next_step"
DBC_PAGE_IN_DOCUMENT: str = "page_in_document"
DBC_PARA_IN_PAGE: str = "para_in_page"
DBC_RUN_ID: str = "run_id"
DBC_SENTENCE_IN_PARA: str = "sentence_in_para"
DBC_SHA256: str = "sha256"
DBC_STATUS: str = "status"
DBC_STEM_NAME: str = "stem_name"
DBC_TOKEN_IN_LINE: str = "token_in_line"
DBC_TOKEN_IN_SENTENCE: str = "token_in_sentence"
DBC_TOKEN_LEMMA: str = "token_lemma"
DBC_TOKEN_PARSED: str = "token_parsed"
DBC_TOKEN_STEM: str = "token_stem"
DBC_TOTAL_ERRONEOUS: str = "total_erroneous"
DBC_TOTAL_OK_PROCESSED: str = "total_ok_processed"
DBC_TOTAL_TO_BE_PROCESSED: str = "total_to_be_processed"
DBC_VERSION: str = "version"

DBT_CONTENT: str = "content"
DBT_DOCUMENT: str = "document"
DBT_JOURNAL: str = "journal"
DBT_LANGUAGE: str = "language"
DBT_RUN: str = "run"
DBT_VERSION: str = "version"

DOCUMENT_DIRECTORY_TYPE_INBOX: str = "inbox"
DOCUMENT_DIRECTORY_TYPE_INBOX_ACCEPTED: str = "inbox_accepted"
DOCUMENT_DIRECTORY_TYPE_INBOX_REJECTED: str = "inbox_rejected"

DOCUMENT_ERROR_CODE_REJ_ERROR: str = "rejected_error"
DOCUMENT_ERROR_CODE_REJ_FILE_DUPL: str = "Duplicate file"
DOCUMENT_ERROR_CODE_REJ_FILE_ERROR: str = "rejected_file_error"
DOCUMENT_ERROR_CODE_REJ_FILE_EXT: str = "Unknown file extension"
DOCUMENT_ERROR_CODE_REJ_FILE_MOVE: str = "Issue with file move"
DOCUMENT_ERROR_CODE_REJ_FILE_RIGHTS: str = "Issue with file permissions"
DOCUMENT_ERROR_CODE_REJ_NO_PDF_FORMAT: str = "No 'pdf' format"
DOCUMENT_ERROR_CODE_REJ_PANDOC: str = "Issue with Pandoc and TeX Live"
DOCUMENT_ERROR_CODE_REJ_PARSER: str = "Issue with parser"
DOCUMENT_ERROR_CODE_REJ_PDF2IMAGE: str = "Issue with pdf2image"
DOCUMENT_ERROR_CODE_REJ_PDFLIB: str = "Issue with PDFlib TET"
DOCUMENT_ERROR_CODE_REJ_TESSERACT: str = "Issue with Tesseract OCR"

DOCUMENT_FILE_TYPE_JPG: str = "jpg"
DOCUMENT_FILE_TYPE_PANDOC: List[str] = [
    "csv",
    "docx",
    "epub",
    "html",
    "odt",
    "rst",
    "rtf",
]
DOCUMENT_FILE_TYPE_PDF: str = "pdf"
DOCUMENT_FILE_TYPE_PNG: str = "png"
DOCUMENT_FILE_TYPE_TESSERACT: List[str] = [
    "bmp",
    "gif",
    "jp2",
    "jpeg",
    "jpg",
    "png",
    "pnm",
    "tif",
    "tiff",
    "webp",
]
DOCUMENT_FILE_TYPE_TIF: str = "tif"
DOCUMENT_FILE_TYPE_TIFF: str = "tiff"
DOCUMENT_FILE_TYPE_XML: str = "xml"

DOCUMENT_NEXT_STEP_PANDOC: str = "Pandoc & TeX Live"
DOCUMENT_NEXT_STEP_PARSER: str = "Parser"
DOCUMENT_NEXT_STEP_PDF2IMAGE: str = "pdf2image"
DOCUMENT_NEXT_STEP_PDFLIB: str = "PDFlib TET"
DOCUMENT_NEXT_STEP_TESSERACT: str = "Tesseract OCR"

DOCUMENT_STATUS_ABORT: str = "abort"
DOCUMENT_STATUS_END: str = "end"
DOCUMENT_STATUS_ERROR: str = "error"
DOCUMENT_STATUS_START: str = "start"

JSON_NAME_API_VERSION: str = "apiVersion"
JSON_NAME_COLUMN_NAME: str = "columnName"
JSON_NAME_COLUMN_VALUE: str = "columnValue"
JSON_NAME_DATA: str = "data"
JSON_NAME_ROW: str = "row"
JSON_NAME_ROWS: str = "rows"
JSON_NAME_TABLES: str = "tables"
JSON_NAME_TABLE_NAME: str = "tableName"

JOURNAL_ACTION_01_901: str = (
    "01.901 Issue (p_i): Document rejected because of unknown file extension='{extension}'."
)
JOURNAL_ACTION_01_902: str = (
    "01.902 Issue (p_i): Moving '{source_file}' to '{target_file}' "
    + "- error: code='{error_code}' msg='{error_msg}'."
)
JOURNAL_ACTION_01_903: str = (
    "01.903 Issue (p_i): Runtime error with fitz.open() processing of file '{source_file}' "
    + "- error: '{error_msg}'."
)
JOURNAL_ACTION_01_904: str = (
    "01.904 Issue (p_i): File permission with file '{source_file}' "
    + "- error: code='{error_code}' msg='{error_msg}'."
)
JOURNAL_ACTION_01_905: str = (
    "01.905 Issue (p_i): The same file has probably already been processed "
    + "once under the file name '{file_name}'."
)
JOURNAL_ACTION_01_906: str = "01.906 Issue (p_i): The target file '{file_name}' already exists."

JOURNAL_ACTION_21_901: str = (
    "21.901 Issue (p_2_i): The 'pdf' document '{file_name}' cannot be converted to an "
    + "image format - error: '{error_msg}'."
)
JOURNAL_ACTION_21_902: str = (
    "21.902 Issue (p_2_i): The child image file number '{child_no}' with file name "
    + "'{file_name}' cannot be stored "
    + "- error: code='{error_code}' msg='{error_msg}'."
)
JOURNAL_ACTION_21_903: str = "21.903 Issue (p_2_i): The target file '{file_name}' already exists."

JOURNAL_ACTION_31_901: str = (
    "31.901 Issue (n_2_p): Converting the file '{source_file}' to the file "
    + "'{target_file}' with Pandoc and TeX Live failed - output='{output}'."
)
JOURNAL_ACTION_31_902: str = (
    "31.902 Issue (n_2_p): The file '{file_name}' cannot be converted to an "
    + "'pdf' document - error: '{error_msg}'."
)
JOURNAL_ACTION_31_903: str = "31.903 Issue (n_2_p): The target file '{file_name}' already exists."

JOURNAL_ACTION_41_901: str = (
    "41.901 Issue (ocr): Converting the file '{source_file}' to the file "
    + "'{target_file}' with Tesseract OCR failed - "
    + "error type: '{error_type}' - error: '{error}'."
)
JOURNAL_ACTION_41_902: str = (
    "41.902 Issue (ocr): Converting the file '{source_file}' to the file "
    + "'{target_file}' with Tesseract OCR failed - "
    + "error status: '{error_status}' - error: '{error}'."
)
JOURNAL_ACTION_41_903: str = "41.903 Issue (ocr): The target file '{file_name}' already exists."

JOURNAL_ACTION_51_901: str = (
    "51.901 Issue (tet): Issues with opening document '{file_name}' - "
    + "error no: '{error_no}' - api: '{api_name}' - error: '{error}'."
)
JOURNAL_ACTION_51_902: str = (
    "51.902 Issue (tet): TETML data could not be retrieved from document '{file_name}' - "
    + "error no: '{error_no}' - api: '{api_name}' - error: '{error}'."
)
JOURNAL_ACTION_51_903: str = (
    "51.903 Issue (tet): Extracting the text and metadata from file '{file_name}' to file "
    + "'{target_file}' failed: "
    + "error no: '{error_no}' - api: '{api_name}' - error: '{error}'."
)

JOURNAL_ACTION_61_901: str = (
    "61.901 Issue (s_f_p): Unknown child tag '{child_tag}' - " + "in parent tag '{parent_tag}'."
)
JOURNAL_ACTION_61_902: str = (
    "61.902 Issue (s_f_p): Expected tag '{expected_tag}' - " + " but found tag '{found_tag}'."
)
JOURNAL_ACTION_61_903: str = (
    "61.903 Issue (s_f_p): Token missing: document {document_id} page {page_no} "
    + "paragraph {para_no} line {line_no}."
)

RUN_STATUS_END: str = "end"
RUN_STATUS_START: str = "start"

# -----------------------------------------------------------------------------
# Global Constants.
# -----------------------------------------------------------------------------

db_current_database: str
db_current_user: str
db_driver_conn: connection | None = None
db_driver_cur: cursor | None = None
db_orm_engine: Engine | None = None
db_orm_metadata: MetaData | None = None
