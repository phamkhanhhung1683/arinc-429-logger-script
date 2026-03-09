def transform_message(raw_message):
    if not raw_message:
        return None
    
    bin_label = raw_message['fields']['label']
    reversed_label = bin_label[::-1]
    processed_label = format(int(reversed_label, 2), '03o')

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
        }
    }

    return processed_message
