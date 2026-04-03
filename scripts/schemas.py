from typing import TypedDict


class RawMessage(TypedDict):
    timestamp: str
    string: str
    channel: int
    binary: str
    parity: str
    data: str
    label: str


class ProcessedMessage(TypedDict):
    raw_message: RawMessage
    parity_ok: bool
    label: str
    message_group: str
    message_description: str
    data: str
