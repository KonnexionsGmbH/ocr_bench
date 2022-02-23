"""Library Stub.

Returns:
    [type]: None.
"""
import pathlib

def get_sha256(file: pathlib.Path) -> str: ...
def progress_msg(msg: str) -> None: ...
def progress_msg_connected() -> None: ...
def progress_msg_disconnected() -> None: ...
def progress_msg_empty_before(msg: str) -> None: ...
def terminate_fatal(error_msg: str) -> None: ...
