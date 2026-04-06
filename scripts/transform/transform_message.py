from scripts.transform.check_parity import get_parity_check
from scripts.transform.process_data import get_processed_data
from scripts.transform.process_label import (
    get_processed_label,
    get_message_group,
    get_message_description,
)
from scripts.schemas import RawMessage, ProcessedMessage


def transform_message(
    raw_message: RawMessage, selected_message_group: str | None
) -> ProcessedMessage | None:
    if not raw_message:
        return None

    parity_ok = get_parity_check(raw_message["binary"])

    processed_label = get_processed_label(raw_message["label"])

    message_group = None
    message_description = None
    processed_data = None

    if processed_label and selected_message_group:
        message_group = get_message_group(selected_message_group, processed_label)
        if message_group:
            message_description = get_message_description(message_group, processed_label)
            processed_data = get_processed_data(message_group, processed_label, raw_message["data"])

    return {
        "raw_message": raw_message,
        "parity_ok": parity_ok,
        "label": processed_label,
        "message_group": message_group,
        "message_description": message_description,
        "data": processed_data,
    }
