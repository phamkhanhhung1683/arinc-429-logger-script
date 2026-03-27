from decimal import Decimal, getcontext


getcontext().prec = 40


def get_processed_data(
    binary_str: str,
    start_pos: int,
    end_pos: int,
    min_val: float,
    max_val: float
) -> str | None:
    if max_val < min_val:
        return None
    
    if not (0 <= start_pos < end_pos <= len(binary_str)):
        return None
    bit_count = end_pos - start_pos

    sub_str = binary_str[start_pos:end_pos]

    try:
        raw_val = int(sub_str, 2)
    except ValueError:
        return None
        
    min_decimal = Decimal(str(min_val))
    max_decimal = Decimal(str(max_val))
    
    scale = (max_decimal - min_decimal) / (Decimal(2) ** bit_count)

    result = (scale * Decimal(raw_val)).normalize() + min_decimal

    return format(result, 'f')


def transform_message(raw_message):
    if not raw_message:
        return None

    bin_label = raw_message['fields']['label']
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

    raw_data = raw_message['fields']['data']
    processed_data = None
    match processed_label:
        case "210" | "211":
            processed_data = get_processed_data(raw_data, 2, 23, 0, 90 * 2)

        case "223":
            processed_data = get_processed_data(raw_data, 2, 23, 0, 65536 * 2)

        case "266" | "267" | "264":
            processed_data = get_processed_data(raw_data, 2, 23, 0, 3034.3168 * 2)

        case "127":
            processed_data = get_processed_data(raw_data, 2, 23, 0, 104857.6 * 2)

        case "320":
            processed_data = get_processed_data(raw_data, 2, 17, 0, 16384 * 2)

    processed_message = {
        "channel": raw_message['channel'],
        "raw_message": raw_message['binary'],
        "raw_fields": {
            "label": raw_message['fields']['label'],
            "data": raw_message['fields']['data'],
            "parity": raw_message['fields']['parity'],
        },
        "processed_fields": {
            "label": processed_label,
            "data": processed_data
        },
        "message_group": message_group
    }

    return processed_message
