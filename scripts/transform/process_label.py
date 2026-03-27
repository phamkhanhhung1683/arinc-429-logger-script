def process_label(raw_label: str) -> str | None:
    reversed_raw_label = raw_label[::-1]

    try:    
        return format(int(reversed_raw_label, 2), '03o')
    except ValueError:
        return None


def get_message_group(processed_label: str) -> str | None:
    A_737_LABELS = {
        "317", "210", "211", "010", "223", "266",
        "267", "264", "324", "127", "320", "126",
        "031", "030", "377", "153"
    }

    if processed_label in A_737_LABELS:
        return "A-737"
    else:
        return None
