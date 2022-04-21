"""Library Stub."""
from typing import Dict
from typing import Iterable

def debug_xml_element_all(
    event: str, parent_tag: str, attrib: Dict[str, str], text: Iterable[str | None]
) -> None: ...
def debug_xml_element_text() -> None: ...
def init_parse_result() -> None: ...
def insert_content() -> None: ...
def parse_tag_box(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_content(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_doc_info(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_document(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_font(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_fonts(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_glyph(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_line(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_page(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_pages(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_para(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_resources(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_text(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tag_word(parent_tag: str, parent: Iterable[str]) -> None: ...
def parse_tetml() -> None: ...
def parse_tetml_file() -> None: ...
