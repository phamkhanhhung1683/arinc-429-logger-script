from .process_data import get_processed_data
from .process_label import (
    get_processed_label,
    get_message_group,
    get_message_description,
)
from scripts.schemas import RawMessage, ProcessedMessage


def transform_message(raw_message: RawMessage) -> ProcessedMessage | None:
    if not raw_message:
        return None

    processed_label = get_processed_label(raw_message["label"])

    message_group = get_message_group(processed_label)

    message_description = get_message_description(processed_label)

    processed_data = get_processed_data(processed_label, raw_message["data"])

    return {
        "raw_message": raw_message,
        "label": processed_label,
        "message_group": message_group,
        "message_description": message_description,
        "data": processed_data,
    }
