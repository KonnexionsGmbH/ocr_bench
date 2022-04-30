"""Library Stub."""
import typing

import spacy
import sqlalchemy

def get_text_from_page_lines(page_data: typing.Dict[str, str | typing.List[typing.Dict[str, int | str]]]) -> str: ...
def tokenize() -> None: ...
def tokenize_document(nlp: spacy.Language, dbt_content: sqlalchemy.Table) -> None: ...
