"""Module cfg.cls_setup: Managing the application configuration parameters."""
from __future__ import annotations

import configparser
import os
from typing import ClassVar
from typing import Dict

import cfg.glob
import utils


# pylint: disable=C0302
# pylint: disable=R0902
# pylint: disable=R0903
# pylint: disable=R0915
class Setup:
    """Managing the application configuration parameters.

    Returns:
        _type_: Application configuration parameters.
    """

    # -----------------------------------------------------------------------------
    # Class variables.
    # -----------------------------------------------------------------------------
    _CONFIG_PARAM_NO: int = 86

    _DCR_CFG_DB_CONNECTION_PORT: ClassVar[str] = "db_connection_port"
    _DCR_CFG_DB_CONNECTION_PREFIX: ClassVar[str] = "db_connection_prefix"
    _DCR_CFG_DB_CONTAINER_PORT: ClassVar[str] = "db_container_port"
    _DCR_CFG_DB_DATABASE: ClassVar[str] = "db_database"
    _DCR_CFG_DB_DATABASE_ADMIN: ClassVar[str] = "db_database_admin"
    _DCR_CFG_DB_DIALECT: ClassVar[str] = "db_dialect"
    _DCR_CFG_DB_HOST: ClassVar[str] = "db_host"
    _DCR_CFG_DB_PASSWORD: ClassVar[str] = "db_password"
    _DCR_CFG_DB_PASSWORD_ADMIN: ClassVar[str] = "db_password_admin"
    _DCR_CFG_DB_SCHEMA: ClassVar[str] = "db_schema"
    _DCR_CFG_DB_USER: ClassVar[str] = "db_user"
    _DCR_CFG_DB_USER_ADMIN: ClassVar[str] = "db_user_admin"
    _DCR_CFG_DCR_VERSION: ClassVar[str] = "dcr_version"
    _DCR_CFG_DELETE_AUXILIARY_FILES: ClassVar[str] = "delete_auxiliary_files"
    _DCR_CFG_DIRECTORY_INBOX: ClassVar[str] = "directory_inbox"
    _DCR_CFG_DIRECTORY_INBOX_ACCEPTED: ClassVar[str] = "directory_inbox_accepted"
    _DCR_CFG_DIRECTORY_INBOX_REJECTED: ClassVar[str] = "directory_inbox_rejected"
    _DCR_CFG_FILE: ClassVar[str] = "setup.cfg"
    _DCR_CFG_IGNORE_DUPLICATES: ClassVar[str] = "ignore_duplicates"
    _DCR_CFG_INITIAL_DATABASE_DATA: ClassVar[str] = "initial_database_data"
    _DCR_CFG_LINE_FOOTER_MAX_DISTANCE: ClassVar[str] = "line_footer_max_distance"
    _DCR_CFG_LINE_FOOTER_MAX_LINES: ClassVar[str] = "line_footer_max_lines"
    _DCR_CFG_LINE_FOOTER_PREFERENCE: ClassVar[str] = "line_footer_preference"
    _DCR_CFG_LINE_HEADER_MAX_DISTANCE: ClassVar[str] = "line_header_max_distance"
    _DCR_CFG_LINE_HEADER_MAX_LINES: ClassVar[str] = "line_header_max_lines"
    _DCR_CFG_PDF2IMAGE_TYPE: ClassVar[str] = "pdf2image_type"
    _DCR_CFG_SECTION: ClassVar[str] = "dcr"
    _DCR_CFG_SECTION_ENV_TEST: ClassVar[str] = "dcr.env.test"
    _DCR_CFG_SECTION_SPACY: ClassVar[str] = "dcr.spacy"

    _DCR_CFG_SPACY_TKN_ATTR_CLUSTER: ClassVar[str] = "spacy_tkn_attr_cluster"
    _DCR_CFG_SPACY_TKN_ATTR_DEP_: ClassVar[str] = "spacy_tkn_attr_dep_"
    _DCR_CFG_SPACY_TKN_ATTR_DOC: ClassVar[str] = "spacy_tkn_attr_doc"
    _DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_: ClassVar[str] = "spacy_tkn_attr_ent_iob_"
    _DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_: ClassVar[str] = "spacy_tkn_attr_ent_kb_id_"
    _DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_: ClassVar[str] = "spacy_tkn_attr_ent_type_"
    _DCR_CFG_SPACY_TKN_ATTR_HEAD: ClassVar[str] = "spacy_tkn_attr_head"
    _DCR_CFG_SPACY_TKN_ATTR_I: ClassVar[str] = "spacy_tkn_attr_i"
    _DCR_CFG_SPACY_TKN_ATTR_IDX: ClassVar[str] = "spacy_tkn_attr_idx"
    _DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA: ClassVar[str] = "spacy_tkn_attr_is_alpha"
    _DCR_CFG_SPACY_TKN_ATTR_IS_ASCII: ClassVar[str] = "spacy_tkn_attr_is_ascii"
    _DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET: ClassVar[str] = "spacy_tkn_attr_is_bracket"
    _DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY: ClassVar[str] = "spacy_tkn_attr_is_currency"
    _DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT: ClassVar[str] = "spacy_tkn_attr_is_digit"
    _DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT: ClassVar[str] = "spacy_tkn_attr_is_left_punct"
    _DCR_CFG_SPACY_TKN_ATTR_IS_LOWER: ClassVar[str] = "spacy_tkn_attr_is_lower"
    _DCR_CFG_SPACY_TKN_ATTR_IS_OOV: ClassVar[str] = "spacy_tkn_attr_is_oov"
    _DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT: ClassVar[str] = "spacy_tkn_attr_is_punct"
    _DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE: ClassVar[str] = "spacy_tkn_attr_is_quote"
    _DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT: ClassVar[str] = "spacy_tkn_attr_is_right_punct"
    _DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END: ClassVar[str] = "spacy_tkn_attr_is_sent_end"
    _DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START: ClassVar[str] = "spacy_tkn_attr_is_sent_start"
    _DCR_CFG_SPACY_TKN_ATTR_IS_SPACE: ClassVar[str] = "spacy_tkn_attr_is_space"
    _DCR_CFG_SPACY_TKN_ATTR_IS_STOP: ClassVar[str] = "spacy_tkn_attr_is_stop"
    _DCR_CFG_SPACY_TKN_ATTR_IS_TITLE: ClassVar[str] = "spacy_tkn_attr_is_title"
    _DCR_CFG_SPACY_TKN_ATTR_IS_UPPER: ClassVar[str] = "spacy_tkn_attr_is_upper"
    _DCR_CFG_SPACY_TKN_ATTR_LANG_: ClassVar[str] = "spacy_tkn_attr_lang_"
    _DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE: ClassVar[str] = "spacy_tkn_attr_left_edge"
    _DCR_CFG_SPACY_TKN_ATTR_LEMMA_: ClassVar[str] = "spacy_tkn_attr_lemma_"
    _DCR_CFG_SPACY_TKN_ATTR_LEX: ClassVar[str] = "spacy_tkn_attr_lex"
    _DCR_CFG_SPACY_TKN_ATTR_LEX_ID: ClassVar[str] = "spacy_tkn_attr_lex_id"
    _DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL: ClassVar[str] = "spacy_tkn_attr_like_email"
    _DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM: ClassVar[str] = "spacy_tkn_attr_like_num"
    _DCR_CFG_SPACY_TKN_ATTR_LIKE_URL: ClassVar[str] = "spacy_tkn_attr_like_url"
    _DCR_CFG_SPACY_TKN_ATTR_LOWER_: ClassVar[str] = "spacy_tkn_attr_lower_"
    _DCR_CFG_SPACY_TKN_ATTR_MORPH: ClassVar[str] = "spacy_tkn_attr_morph"
    _DCR_CFG_SPACY_TKN_ATTR_NORM_: ClassVar[str] = "spacy_tkn_attr_norm_"
    _DCR_CFG_SPACY_TKN_ATTR_ORTH_: ClassVar[str] = "spacy_tkn_attr_orth_"
    _DCR_CFG_SPACY_TKN_ATTR_POS_: ClassVar[str] = "spacy_tkn_attr_pos_"
    _DCR_CFG_SPACY_TKN_ATTR_PREFIX_: ClassVar[str] = "spacy_tkn_attr_prefix_"
    _DCR_CFG_SPACY_TKN_ATTR_PROB: ClassVar[str] = "spacy_tkn_attr_prob"
    _DCR_CFG_SPACY_TKN_ATTR_RANK: ClassVar[str] = "spacy_tkn_attr_rank"
    _DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE: ClassVar[str] = "spacy_tkn_attr_right_edge"
    _DCR_CFG_SPACY_TKN_ATTR_SENT: ClassVar[str] = "spacy_tkn_attr_sent"
    _DCR_CFG_SPACY_TKN_ATTR_SENTIMENT: ClassVar[str] = "spacy_tkn_attr_sentiment"
    _DCR_CFG_SPACY_TKN_ATTR_SHAPE_: ClassVar[str] = "spacy_tkn_attr_shape_"
    _DCR_CFG_SPACY_TKN_ATTR_SUFFIX_: ClassVar[str] = "spacy_tkn_attr_suffix_"
    _DCR_CFG_SPACY_TKN_ATTR_TAG_: ClassVar[str] = "spacy_tkn_attr_tag_"
    _DCR_CFG_SPACY_TKN_ATTR_TENSOR: ClassVar[str] = "spacy_tkn_attr_tensor"
    _DCR_CFG_SPACY_TKN_ATTR_TEXT: ClassVar[str] = "spacy_tkn_attr_text"
    _DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS: ClassVar[str] = "spacy_tkn_attr_text_with_ws"
    _DCR_CFG_SPACY_TKN_ATTR_VOCAB: ClassVar[str] = "spacy_tkn_attr_vocab"
    _DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_: ClassVar[str] = "spacy_tkn_attr_whitespace_"

    _DCR_CFG_TESSERACT_TIMEOUT: ClassVar[str] = "tesseract_timeout"
    _DCR_CFG_TETML_PAGE: ClassVar[str] = "tetml_page"
    _DCR_CFG_TETML_WORD: ClassVar[str] = "tetml_word"
    _DCR_CFG_TOKENIZE_2_DATABASE: ClassVar[str] = "tokenize_2_database"
    _DCR_CFG_TOKENIZE_2_JSONFILE: ClassVar[str] = "tokenize_2_jsonfile"
    _DCR_CFG_VERBOSE: ClassVar[str] = "verbose"
    _DCR_CFG_VERBOSE_LINE_TYPE: ClassVar[str] = "verbose_line_type"
    _DCR_CFG_VERBOSE_PARSER: ClassVar[str] = "verbose_parser"

    _DCR_ENVIRONMENT_TYPE: ClassVar[str] = "DCR_ENVIRONMENT_TYPE"

    _ENVIRONMENT_TYPE_DEV: ClassVar[str] = "dev"
    _ENVIRONMENT_TYPE_PROD: ClassVar[str] = "prod"
    _ENVIRONMENT_TYPE_TEST: ClassVar[str] = "test"

    PDF2IMAGE_TYPE_JPEG: ClassVar[str] = "jpeg"
    PDF2IMAGE_TYPE_PNG: ClassVar[str] = "png"

    # -----------------------------------------------------------------------------
    # Initialise the instance.
    # -----------------------------------------------------------------------------
    def __init__(self) -> None:  # pylint: disable=too-many-statements
        """Initialise the instance."""
        cfg.glob.logger.debug(cfg.glob.LOGGER_START)

        self._get_environment_variant()

        self._config: Dict[str, str] = {}

        self.db_connection_port: str = ""
        self.db_connection_prefix: str = "postgresql+psycopg2://"
        self.db_container_port: str = ""
        self.db_database: str = ""
        self.db_database_admin: str = ""
        self.db_dialect: str = "postgresql"
        self.db_host: str = "localhost"
        self.db_password: str | None = None
        self.db_password_admin: str | None = None
        self.db_schema: str = "dcr_schema"
        self.db_user: str = "postgresql"
        self.db_user_admin: str = "postgresql"
        self.dcr_version: str = "0.9.2"
        self.directory_inbox: str = utils.get_os_independent_name("data/inbox")
        self.directory_inbox_accepted: str = utils.get_os_independent_name("data/inbox_accepted")
        self.directory_inbox_rejected: str = utils.get_os_independent_name("data/inbox_rejected")
        self.initial_database_data: str = utils.get_os_independent_name("data/initial_database_data.json")
        self.is_delete_auxiliary_files: bool = True
        self.is_ignore_duplicates: bool = False
        self.is_line_footer_preferred: bool = True
        self.is_spacy_tkn_attr_cluster: bool = False
        self.is_spacy_tkn_attr_dep_: bool = False
        self.is_spacy_tkn_attr_doc: bool = False
        self.is_spacy_tkn_attr_ent_iob_: bool = False
        self.is_spacy_tkn_attr_ent_kb_id_: bool = False
        self.is_spacy_tkn_attr_ent_type_: bool = True
        self.is_spacy_tkn_attr_head: bool = False
        self.is_spacy_tkn_attr_i: bool = True
        self.is_spacy_tkn_attr_idx: bool = False
        self.is_spacy_tkn_attr_is_alpha: bool = False
        self.is_spacy_tkn_attr_is_ascii: bool = False
        self.is_spacy_tkn_attr_is_bracket: bool = False
        self.is_spacy_tkn_attr_is_currency: bool = True
        self.is_spacy_tkn_attr_is_digit: bool = True
        self.is_spacy_tkn_attr_is_left_punct: bool = False
        self.is_spacy_tkn_attr_is_lower: bool = False
        self.is_spacy_tkn_attr_is_oov: bool = True
        self.is_spacy_tkn_attr_is_punct: bool = True
        self.is_spacy_tkn_attr_is_quote: bool = False
        self.is_spacy_tkn_attr_is_right_punct: bool = False
        self.is_spacy_tkn_attr_is_sent_end: bool = False
        self.is_spacy_tkn_attr_is_sent_start: bool = False
        self.is_spacy_tkn_attr_is_space: bool = False
        self.is_spacy_tkn_attr_is_stop: bool = True
        self.is_spacy_tkn_attr_is_title: bool = True
        self.is_spacy_tkn_attr_is_upper: bool = False
        self.is_spacy_tkn_attr_lang_: bool = False
        self.is_spacy_tkn_attr_left_edge: bool = False
        self.is_spacy_tkn_attr_lemma_: bool = True
        self.is_spacy_tkn_attr_lex: bool = False
        self.is_spacy_tkn_attr_lex_id: bool = False
        self.is_spacy_tkn_attr_like_email: bool = True
        self.is_spacy_tkn_attr_like_num: bool = True
        self.is_spacy_tkn_attr_like_url: bool = True
        self.is_spacy_tkn_attr_lower_: bool = False
        self.is_spacy_tkn_attr_morph: bool = False
        self.is_spacy_tkn_attr_norm_: bool = True
        self.is_spacy_tkn_attr_orth_: bool = False
        self.is_spacy_tkn_attr_pos_: bool = True
        self.is_spacy_tkn_attr_prefix_: bool = False
        self.is_spacy_tkn_attr_prob: bool = False
        self.is_spacy_tkn_attr_rank: bool = False
        self.is_spacy_tkn_attr_right_edge: bool = False
        self.is_spacy_tkn_attr_sent: bool = False
        self.is_spacy_tkn_attr_sentiment: bool = False
        self.is_spacy_tkn_attr_shape_: bool = False
        self.is_spacy_tkn_attr_suffix_: bool = False
        self.is_spacy_tkn_attr_tag_: bool = True
        self.is_spacy_tkn_attr_tensor: bool = False
        self.is_spacy_tkn_attr_text: bool = True
        self.is_spacy_tkn_attr_text_with_ws: bool = False
        self.is_spacy_tkn_attr_vocab: bool = False
        self.is_spacy_tkn_attr_whitespace_: bool = True
        self.is_tetml_page: bool = False
        self.is_tetml_word: bool = False
        self.is_tokenize_2_database: bool = True
        self.is_tokenize_2_jsonfile: bool = False
        self.is_verbose: bool = True
        self.is_verbose_line_type: bool = False
        self.line_footer_max_distance: int = 3
        self.line_footer_max_lines: int = 3
        self.line_header_max_distance: int = 3
        self.line_header_max_lines: int = 3
        self.pdf2image_type: str = Setup.PDF2IMAGE_TYPE_JPEG
        self.tesseract_timeout: int = 10
        self.verbose_parser: str = "none"

        self._load_config()  # pylint: disable=E1121

        utils.progress_msg_core("The configuration parameters are checked and loaded")

        cfg.glob.logger.debug(cfg.glob.LOGGER_END)

    # -----------------------------------------------------------------------------
    # Check the configuration parameters.
    # -----------------------------------------------------------------------------
    def _check_config(self) -> None:
        """Check the configuration parameters."""
        self._check_config_delete_auxiliary_files()
        self._check_config_directory_inbox()
        self._check_config_directory_inbox_accepted()
        self._check_config_directory_inbox_rejected()
        self._check_config_ignore_duplicates()
        self._check_config_line_footer_preference()
        self._check_config_pdf2image_type()
        self._check_config_spacy_tkn_attr_cluster()
        self._check_config_spacy_tkn_attr_dep_()
        self._check_config_spacy_tkn_attr_doc()
        self._check_config_spacy_tkn_attr_ent_iob_()
        self._check_config_spacy_tkn_attr_ent_kb_id_()
        self._check_config_spacy_tkn_attr_ent_type_()
        self._check_config_spacy_tkn_attr_head()
        self._check_config_spacy_tkn_attr_i()
        self._check_config_spacy_tkn_attr_idx()
        self._check_config_spacy_tkn_attr_is_alpha()
        self._check_config_spacy_tkn_attr_is_ascii()
        self._check_config_spacy_tkn_attr_is_bracket()
        self._check_config_spacy_tkn_attr_is_currency()
        self._check_config_spacy_tkn_attr_is_digit()
        self._check_config_spacy_tkn_attr_is_left_punct()
        self._check_config_spacy_tkn_attr_is_lower()
        self._check_config_spacy_tkn_attr_is_oov()
        self._check_config_spacy_tkn_attr_is_punct()
        self._check_config_spacy_tkn_attr_is_quote()
        self._check_config_spacy_tkn_attr_is_right_punct()
        self._check_config_spacy_tkn_attr_is_sent_end()
        self._check_config_spacy_tkn_attr_is_sent_start()
        self._check_config_spacy_tkn_attr_is_space()
        self._check_config_spacy_tkn_attr_is_stop()
        self._check_config_spacy_tkn_attr_is_title()
        self._check_config_spacy_tkn_attr_is_upper()
        self._check_config_spacy_tkn_attr_lang_()
        self._check_config_spacy_tkn_attr_left_edge()
        self._check_config_spacy_tkn_attr_lemma_()
        self._check_config_spacy_tkn_attr_lex()
        self._check_config_spacy_tkn_attr_lex_id()
        self._check_config_spacy_tkn_attr_like_email()
        self._check_config_spacy_tkn_attr_like_num()
        self._check_config_spacy_tkn_attr_like_url()
        self._check_config_spacy_tkn_attr_lower_()
        self._check_config_spacy_tkn_attr_morph()
        self._check_config_spacy_tkn_attr_norm_()
        self._check_config_spacy_tkn_attr_orth_()
        self._check_config_spacy_tkn_attr_pos_()
        self._check_config_spacy_tkn_attr_prefix_()
        self._check_config_spacy_tkn_attr_prob()
        self._check_config_spacy_tkn_attr_rank()
        self._check_config_spacy_tkn_attr_right_edge()
        self._check_config_spacy_tkn_attr_sent()
        self._check_config_spacy_tkn_attr_sentiment()
        self._check_config_spacy_tkn_attr_shape_()
        self._check_config_spacy_tkn_attr_suffix_()
        self._check_config_spacy_tkn_attr_tag_()
        self._check_config_spacy_tkn_attr_tensor()
        self._check_config_spacy_tkn_attr_text()
        self._check_config_spacy_tkn_attr_text_with_ws()
        self._check_config_spacy_tkn_attr_vocab()
        self._check_config_spacy_tkn_attr_whitespace_()
        self._check_config_tesseract_timeout()
        self._check_config_tetml_page()
        self._check_config_tetml_word()
        self._check_config_tokenize_2_database()
        self._check_config_tokenize_2_jsonfile()
        self._check_config_verbose()
        self._check_config_verbose_line_type()
        self._check_config_verbose_parser()

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - delete_auxiliary_files.
    # -----------------------------------------------------------------------------
    def _check_config_delete_auxiliary_files(self) -> None:
        """Check the configuration parameter - delete_auxiliary_files."""
        if Setup._DCR_CFG_DELETE_AUXILIARY_FILES in self._config:
            if str(self._config[Setup._DCR_CFG_DELETE_AUXILIARY_FILES]).lower() == "false":
                self.is_delete_auxiliary_files = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - directory_inbox.
    # -----------------------------------------------------------------------------
    def _check_config_directory_inbox(self) -> None:
        """Check the configuration parameter - directory_inbox."""
        if Setup._DCR_CFG_DIRECTORY_INBOX in self._config:
            self._config[Setup._DCR_CFG_DIRECTORY_INBOX] = str(self._config[Setup._DCR_CFG_DIRECTORY_INBOX])

            self.directory_inbox = utils.get_os_independent_name(str(self._config[Setup._DCR_CFG_DIRECTORY_INBOX]))
        else:
            utils.terminate_fatal_setup(f"Missing configuration parameter '{Setup._DCR_CFG_DIRECTORY_INBOX}'")

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - directory_inbox_accepted.
    # -----------------------------------------------------------------------------
    def _check_config_directory_inbox_accepted(self) -> None:
        """Check the configuration parameter - directory_inbox_accepted."""
        if Setup._DCR_CFG_DIRECTORY_INBOX_ACCEPTED in self._config:
            self._config[Setup._DCR_CFG_DIRECTORY_INBOX_ACCEPTED] = str(
                self._config[Setup._DCR_CFG_DIRECTORY_INBOX_ACCEPTED]
            )

            self.directory_inbox_accepted = utils.get_os_independent_name(
                str(self._config[Setup._DCR_CFG_DIRECTORY_INBOX_ACCEPTED])
            )
        else:
            utils.terminate_fatal_setup(f"Missing configuration parameter '{Setup._DCR_CFG_DIRECTORY_INBOX_ACCEPTED}'")

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - directory_inbox_rejected.
    # -----------------------------------------------------------------------------
    def _check_config_directory_inbox_rejected(self) -> None:
        """Check the configuration parameter - directory_inbox_rejected."""
        if Setup._DCR_CFG_DIRECTORY_INBOX_REJECTED in self._config:
            self._config[Setup._DCR_CFG_DIRECTORY_INBOX_REJECTED] = str(
                self._config[Setup._DCR_CFG_DIRECTORY_INBOX_REJECTED]
            )

            self.directory_inbox_rejected = utils.get_os_independent_name(
                str(self._config[Setup._DCR_CFG_DIRECTORY_INBOX_REJECTED])
            )
        else:
            utils.terminate_fatal_setup(f"Missing configuration parameter '{Setup._DCR_CFG_DIRECTORY_INBOX_REJECTED}'")

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - ignore_duplicates.
    # -----------------------------------------------------------------------------
    def _check_config_ignore_duplicates(self) -> None:
        """Check the configuration parameter - ignore_duplicates."""
        if Setup._DCR_CFG_IGNORE_DUPLICATES in self._config:
            if str(self._config[Setup._DCR_CFG_IGNORE_DUPLICATES]).lower() == "true":
                self.is_ignore_duplicates = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - line_footer_preference.
    # -----------------------------------------------------------------------------
    def _check_config_line_footer_preference(self) -> None:
        """Check the configuration parameter - line_footer_preference."""
        if Setup._DCR_CFG_LINE_FOOTER_PREFERENCE in self._config:
            if str(self._config[Setup._DCR_CFG_LINE_FOOTER_PREFERENCE]).lower() == "false":
                self.is_line_footer_preferred = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - pdf2image_type.
    # -----------------------------------------------------------------------------
    def _check_config_pdf2image_type(self) -> None:
        """Check the configuration parameter - pdf2image_type."""
        if Setup._DCR_CFG_PDF2IMAGE_TYPE in self._config:
            self.pdf2image_type = str(self._config[Setup._DCR_CFG_PDF2IMAGE_TYPE])
            if self.pdf2image_type not in [
                Setup.PDF2IMAGE_TYPE_JPEG,
                Setup.PDF2IMAGE_TYPE_PNG,
            ]:
                utils.terminate_fatal_setup(
                    f"Invalid configuration parameter value for parameter " f"'pdf2image_type': '{self.pdf2image_type}'"
                )

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_cluster.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_cluster(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_cluster."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER]).lower() == "true":
                self.is_spacy_tkn_attr_cluster = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_dep_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_dep_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_dep_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_DEP_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_DEP_]).lower() == "true":
                self.is_spacy_tkn_attr_dep_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_doc.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_doc(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_doc."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_DOC in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_DOC]).lower() == "true":
                self.is_spacy_tkn_attr_doc = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_ent_iob_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_ent_iob_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_ent_iob_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_]).lower() == "true":
                self.is_spacy_tkn_attr_ent_iob_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_ent_kb_id_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_ent_kb_id_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_ent_kb_id_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_]).lower() == "true":
                self.is_spacy_tkn_attr_ent_kb_id_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - ent_type_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_ent_type_(self) -> None:
        """Check the configuration parameter - ent_type_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_]).lower() == "false":
                self.is_spacy_tkn_attr_ent_type_ = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_head.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_head(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_head."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_HEAD in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_HEAD]).lower() == "true":
                self.is_spacy_tkn_attr_head = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - i.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_i(self) -> None:
        """Check the configuration parameter - i."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_I in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_I]).lower() == "false":
                self.is_spacy_tkn_attr_i = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_idx.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_idx(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_idx."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IDX in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IDX]).lower() == "true":
                self.is_spacy_tkn_attr_idx = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_alpha.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_alpha(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_alpha."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA]).lower() == "true":
                self.is_spacy_tkn_attr_is_alpha = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_ascii.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_ascii(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_ascii."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII]).lower() == "true":
                self.is_spacy_tkn_attr_is_ascii = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_bracket.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_bracket(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_bracket."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET]).lower() == "true":
                self.is_spacy_tkn_attr_is_bracket = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - is_currency.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_currency(self) -> None:
        """Check the configuration parameter - is_currency."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY]).lower() == "false":
                self.is_spacy_tkn_attr_is_currency = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - is_digit.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_digit(self) -> None:
        """Check the configuration parameter - is_digit."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT]).lower() == "false":
                self.is_spacy_tkn_attr_is_digit = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_left_punct.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_left_punct(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_left_punct."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT]).lower() == "true":
                self.is_spacy_tkn_attr_is_left_punct = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_lower.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_lower(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_lower."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER]).lower() == "true":
                self.is_spacy_tkn_attr_is_lower = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - is_oov.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_oov(self) -> None:
        """Check the configuration parameter - is_oov."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV]).lower() == "false":
                self.is_spacy_tkn_attr_is_oov = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - is_punct.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_punct(self) -> None:
        """Check the configuration parameter - is_punct."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT]).lower() == "false":
                self.is_spacy_tkn_attr_is_punct = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_quote.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_quote(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_quote."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE]).lower() == "true":
                self.is_spacy_tkn_attr_is_quote = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_right_punct.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_right_punct(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_right_punct."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT]).lower() == "true":
                self.is_spacy_tkn_attr_is_right_punct = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_sent_end.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_sent_end(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_sent_end."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END]).lower() == "true":
                self.is_spacy_tkn_attr_is_sent_end = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_sent_start.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_sent_start(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_sent_start."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START]).lower() == "true":
                self.is_spacy_tkn_attr_is_sent_start = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_space.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_space(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_space."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE]).lower() == "true":
                self.is_spacy_tkn_attr_is_space = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - is_stop.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_stop(self) -> None:
        """Check the configuration parameter - is_stop."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP]).lower() == "false":
                self.is_spacy_tkn_attr_is_stop = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - is_title.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_title(self) -> None:
        """Check the configuration parameter - is_title."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE]).lower() == "false":
                self.is_spacy_tkn_attr_is_title = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_is_upper.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_is_upper(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_is_upper."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER]).lower() == "true":
                self.is_spacy_tkn_attr_is_upper = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_lang_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_lang_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_lang_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LANG_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LANG_]).lower() == "true":
                self.is_spacy_tkn_attr_lang_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_left_edge.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_left_edge(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_left_edge."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE]).lower() == "true":
                self.is_spacy_tkn_attr_left_edge = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - lemma_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_lemma_(self) -> None:
        """Check the configuration parameter - lemma_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_]).lower() == "false":
                self.is_spacy_tkn_attr_lemma_ = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_lex.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_lex(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_lex."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEX in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LEX]).lower() == "true":
                self.is_spacy_tkn_attr_lex = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_lex_id.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_lex_id(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_lex_id."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID]).lower() == "true":
                self.is_spacy_tkn_attr_lex_id = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - like_email.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_like_email(self) -> None:
        """Check the configuration parameter - like_email."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL]).lower() == "false":
                self.is_spacy_tkn_attr_like_email = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - like_num.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_like_num(self) -> None:
        """Check the configuration parameter - like_num."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM]).lower() == "false":
                self.is_spacy_tkn_attr_like_num = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - like_url.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_like_url(self) -> None:
        """Check the configuration parameter - like_url."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL]).lower() == "false":
                self.is_spacy_tkn_attr_like_url = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_lower_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_lower_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_lower_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_]).lower() == "true":
                self.is_spacy_tkn_attr_lower_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_morph.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_morph(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_morph."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_MORPH in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_MORPH]).lower() == "true":
                self.is_spacy_tkn_attr_morph = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - norm_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_norm_(self) -> None:
        """Check the configuration parameter - norm_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_NORM_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_NORM_]).lower() == "false":
                self.is_spacy_tkn_attr_norm_ = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_orth_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_orth_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_orth_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_]).lower() == "true":
                self.is_spacy_tkn_attr_orth_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - pos_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_pos_(self) -> None:
        """Check the configuration parameter - pos_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_POS_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_POS_]).lower() == "false":
                self.is_spacy_tkn_attr_pos_ = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_prefix_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_prefix_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_prefix_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_]).lower() == "true":
                self.is_spacy_tkn_attr_prefix_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_prob.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_prob(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_prob."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_PROB in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_PROB]).lower() == "true":
                self.is_spacy_tkn_attr_prob = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_rank.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_rank(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_rank."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_RANK in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_RANK]).lower() == "true":
                self.is_spacy_tkn_attr_rank = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_right_edge.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_right_edge(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_right_edge."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE]).lower() == "true":
                self.is_spacy_tkn_attr_right_edge = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_sent.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_sent(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_sent."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_SENT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_SENT]).lower() == "true":
                self.is_spacy_tkn_attr_sent = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_sentiment.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_sentiment(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_sentiment."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT]).lower() == "true":
                self.is_spacy_tkn_attr_sentiment = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_shape_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_shape_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_shape_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_]).lower() == "true":
                self.is_spacy_tkn_attr_shape_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_suffix_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_suffix_(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_suffix_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_]).lower() == "true":
                self.is_spacy_tkn_attr_suffix_ = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - tag_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_tag_(self) -> None:
        """Check the configuration parameter - tag_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_TAG_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_TAG_]).lower() == "false":
                self.is_spacy_tkn_attr_tag_ = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_tensor.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_tensor(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_tensor."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR]).lower() == "true":
                self.is_spacy_tkn_attr_tensor = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - text.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_text(self) -> None:
        """Check the configuration parameter - text."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT]).lower() == "false":
                self.is_spacy_tkn_attr_text = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_vocab.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_vocab(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_vocab."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB]).lower() == "true":
                self.is_spacy_tkn_attr_vocab = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - whitespace_.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_whitespace_(self) -> None:
        """Check the configuration parameter - whitespace_."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_ in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_]).lower() == "false":
                self.is_spacy_tkn_attr_whitespace_ = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - spacy_tkn_attr_text_with_ws.
    # -----------------------------------------------------------------------------
    def _check_config_spacy_tkn_attr_text_with_ws(self) -> None:
        """Check the configuration parameter - spacy_tkn_attr_text_with_ws."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS in self._config:
            if str(self._config[Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS]).lower() == "true":
                self.is_spacy_tkn_attr_text_with_ws = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - tesseract_timeout.
    # -----------------------------------------------------------------------------
    def _check_config_tesseract_timeout(self) -> None:
        """Check the configuration parameter - tesseract_timeout."""
        if Setup._DCR_CFG_TESSERACT_TIMEOUT in self._config:
            self.tesseract_timeout = int(str(self._config[Setup._DCR_CFG_TESSERACT_TIMEOUT]))

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - tetml_page.
    # -----------------------------------------------------------------------------
    def _check_config_tetml_page(self) -> None:
        """Check the configuration parameter - tetml_page."""
        if Setup._DCR_CFG_TETML_PAGE in self._config:
            if str(self._config[Setup._DCR_CFG_TETML_PAGE]).lower() == "true":
                self.is_tetml_page = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - tetml_word.
    # -----------------------------------------------------------------------------
    def _check_config_tetml_word(self) -> None:
        """Check the configuration parameter - tetml_word."""
        if Setup._DCR_CFG_TETML_WORD in self._config:
            if str(self._config[Setup._DCR_CFG_TETML_WORD]).lower() == "true":
                self.is_tetml_word = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - tokenize_2_database.
    # -----------------------------------------------------------------------------
    def _check_config_tokenize_2_database(self) -> None:
        """Check the configuration parameter - tokenize_2_database."""
        if Setup._DCR_CFG_TOKENIZE_2_DATABASE in self._config:
            if str(self._config[Setup._DCR_CFG_TOKENIZE_2_DATABASE]).lower() == "false":
                self.is_tokenize_2_database = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - tokenize_2_jsonfile.
    # -----------------------------------------------------------------------------
    def _check_config_tokenize_2_jsonfile(self) -> None:
        """Check the configuration parameter - tokenize_2_jsonfile."""
        if Setup._DCR_CFG_TOKENIZE_2_JSONFILE in self._config:
            if str(self._config[Setup._DCR_CFG_TOKENIZE_2_JSONFILE]).lower() == "true":
                self.is_tokenize_2_jsonfile = True

        if not self.is_tokenize_2_database:
            if not self.is_tokenize_2_jsonfile:
                utils.terminate_fatal_setup(
                    "At least one of the configuration parameters 'tokenize_2_database' or "
                    + "'tokenize_2_jsonfile' must be 'true'"
                )

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - verbose.
    # -----------------------------------------------------------------------------
    def _check_config_verbose(self) -> None:
        """Check the configuration parameter - verbose."""
        if Setup._DCR_CFG_VERBOSE in self._config:
            if str(self._config[Setup._DCR_CFG_VERBOSE]).lower() == "false":
                self.is_verbose = False

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - verbose_line_type.
    # -----------------------------------------------------------------------------
    def _check_config_verbose_line_type(self) -> None:
        """Check the configuration parameter - verbose_line_type."""
        if Setup._DCR_CFG_VERBOSE_LINE_TYPE in self._config:
            if str(self._config[Setup._DCR_CFG_VERBOSE_LINE_TYPE]).lower() == "true":
                self.is_verbose_line_type = True

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - verbose_parser.
    # -----------------------------------------------------------------------------
    def _check_config_verbose_parser(self) -> None:
        """Check the configuration parameter - verbose_parser."""
        if Setup._DCR_CFG_VERBOSE_PARSER in self._config:
            if str(self._config[Setup._DCR_CFG_VERBOSE_PARSER]).lower() in ["all", "text"]:
                self.verbose_parser = str(self._config[Setup._DCR_CFG_VERBOSE_PARSER]).lower()

    # -----------------------------------------------------------------------------
    # Determine and check the environment variant.
    # -----------------------------------------------------------------------------
    def _get_environment_variant(self) -> None:
        """Determine and check the environment variant."""
        self.environment_variant = Setup._ENVIRONMENT_TYPE_PROD

        try:
            self.environment_variant = os.environ[Setup._DCR_ENVIRONMENT_TYPE]
        except KeyError:
            utils.terminate_fatal_setup(f"The environment variable '{Setup._DCR_ENVIRONMENT_TYPE}' is missing")

        if self.environment_variant not in [
            Setup._ENVIRONMENT_TYPE_DEV,
            Setup._ENVIRONMENT_TYPE_PROD,
            Setup._ENVIRONMENT_TYPE_TEST,
        ]:
            utils.terminate_fatal_setup(
                f"The environment variable '{Setup._DCR_ENVIRONMENT_TYPE}' "
                f"has the invalid content '{self.environment_variant}'"
            )

    # -----------------------------------------------------------------------------
    # Load and check the configuration parameters.
    # -----------------------------------------------------------------------------
    def _load_config(self) -> None:
        """Load and check the configuration parameters."""
        config_parser = configparser.ConfigParser()
        config_parser.read(Setup._DCR_CFG_FILE)

        for section in config_parser.sections():
            if section in (
                Setup._DCR_CFG_SECTION,
                Setup._DCR_CFG_SECTION + ".env." + self.environment_variant,
                Setup._DCR_CFG_SECTION_SPACY,
            ):
                for (key, value) in config_parser.items(section):
                    self._config[key] = value

        for key, item in self._config.items():
            match key:
                case Setup._DCR_CFG_DB_CONNECTION_PORT:
                    self.db_connection_port = str(item)
                case Setup._DCR_CFG_DB_CONNECTION_PREFIX:
                    self.db_connection_prefix = str(item)
                case Setup._DCR_CFG_DB_CONTAINER_PORT:
                    self.db_container_port = str(item)
                case Setup._DCR_CFG_DB_DATABASE:
                    self.db_database = str(item)
                case Setup._DCR_CFG_DB_DATABASE_ADMIN:
                    self.db_database_admin = str(item)
                case Setup._DCR_CFG_DB_DIALECT:
                    self.db_dialect = str(item)
                case Setup._DCR_CFG_DB_HOST:
                    self.db_host = str(item)
                case Setup._DCR_CFG_DB_PASSWORD:
                    self.db_password = str(item)
                case Setup._DCR_CFG_DB_PASSWORD_ADMIN:
                    self.db_password_admin = str(item)
                case Setup._DCR_CFG_DB_SCHEMA:
                    self.db_schema = str(item)
                case Setup._DCR_CFG_DB_USER:
                    self.db_user = str(item)
                case Setup._DCR_CFG_DB_USER_ADMIN:
                    self.db_user_admin = str(item)
                case Setup._DCR_CFG_DCR_VERSION:
                    self.dcr_version = str(item)
                case (
                    Setup._DCR_CFG_DELETE_AUXILIARY_FILES
                    | Setup._DCR_CFG_DIRECTORY_INBOX
                    | Setup._DCR_CFG_DIRECTORY_INBOX_ACCEPTED
                    | Setup._DCR_CFG_DIRECTORY_INBOX_REJECTED
                    | Setup._DCR_CFG_IGNORE_DUPLICATES
                    | Setup._DCR_CFG_LINE_FOOTER_PREFERENCE
                    | Setup._DCR_CFG_PDF2IMAGE_TYPE
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_DEP_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_DOC
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_HEAD
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_I
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IDX
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LANG_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LEX
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_MORPH
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_NORM_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_POS_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_PROB
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_RANK
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_SENT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_TAG_
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB
                    | Setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_
                    | Setup._DCR_CFG_TESSERACT_TIMEOUT
                    | Setup._DCR_CFG_TETML_PAGE
                    | Setup._DCR_CFG_TETML_WORD
                    | Setup._DCR_CFG_TOKENIZE_2_DATABASE
                    | Setup._DCR_CFG_TOKENIZE_2_JSONFILE
                    | Setup._DCR_CFG_VERBOSE
                    | Setup._DCR_CFG_VERBOSE_LINE_TYPE
                    | Setup._DCR_CFG_VERBOSE_PARSER
                ):
                    continue
                case Setup._DCR_CFG_INITIAL_DATABASE_DATA:
                    self.initial_database_data = utils.get_os_independent_name(item)
                case Setup._DCR_CFG_LINE_FOOTER_MAX_DISTANCE:
                    self.line_footer_max_distance = int(item)
                case Setup._DCR_CFG_LINE_FOOTER_MAX_LINES:
                    self.line_footer_max_lines = int(item)
                case Setup._DCR_CFG_LINE_HEADER_MAX_DISTANCE:
                    self.line_header_max_distance = int(item)
                case Setup._DCR_CFG_LINE_HEADER_MAX_LINES:
                    self.line_header_max_lines = int(item)
                case _:
                    utils.terminate_fatal_setup(f"Unknown configuration parameter '{key}'")

        self._check_config()
