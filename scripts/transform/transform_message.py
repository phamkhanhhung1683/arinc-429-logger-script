from .process_data import process_data_by_label
from schemas import RawMessage, ProcessedMessage


def transform_message(raw_message: RawMessage) -> ProcessedMessage | None:
    if not raw_message:
        return None

    bin_label = raw_message['label']
    reversed_label = bin_label[::-1]

    try:    
        processed_label = format(int(reversed_label, 2), '03o')
    except ValueError:
        processed_label = None

    a_737_labels = [ "317", "210", "211", "010", "223", "266", "267", "264", "324", "127", "320", "126", "031", "030", "377", "153"]
    if processed_label in a_737_labels:
        message_group = "A-737"
    else:
        message_group = None

    processed_data = process_data_by_label(processed_label, raw_message['data'])

    return {
        "raw_message": raw_message,
        "label": processed_label,
        "message_group": message_group,
        "data": processed_data,
    }
