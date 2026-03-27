from .process_data import process_data_by_label
from .process_label import process_label, get_message_group
from schemas import RawMessage, ProcessedMessage


def transform_message(raw_message: RawMessage) -> ProcessedMessage | None:
    if not raw_message:
        return None

    processed_label = process_label(raw_message['label'])

    message_group = get_message_group(processed_label)

    processed_data = process_data_by_label(processed_label, raw_message['data'])

    return {
        "raw_message": raw_message,
        "label": processed_label,
        "message_group": message_group,
        "data": processed_data,
    }
