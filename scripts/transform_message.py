def transform_message(raw_message):
    if not raw_message:
        return None

    bin_label = raw_message['fields']['label']
    reversed_label = bin_label[::-1]

    try:    
        processed_label = format(int(reversed_label, 2), '03o')
    except ValueError:
        processed_label = None

    a_737_labels = [ "317", "210", "211", "010", "223", "266", "267", "264", "324", "127", "320", "126", "031", "030", "377", "154"]
    if processed_label in a_737_labels:
        message_group = "A-737"
    else:
        message_group = None

    processed_message = {
        "channel": raw_message['channel'],
        "raw_message": raw_message['binary'],
        "raw_fields": {
            "label": raw_message['fields']['label'],
            "data": raw_message['fields']['data'],
            "ssm": raw_message['fields']['ssm'],
            "parity": raw_message['fields']['parity'],
        },
        "processed_fields": {
            "label": processed_label
        },
        "message_group": message_group
    }

    return processed_message


def binary_to_decimal(bin_str):
    try:
        decimal_val = int(bin_str, 2)
        return decimal_val
    except ValueError as e:
        print(f"[ERROR] Value error: {e}")
        return None
