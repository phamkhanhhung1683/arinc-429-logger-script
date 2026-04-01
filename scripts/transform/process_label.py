from scripts.transform.label_config import LABEL_DESCRIPTIONS, LABEL_GROUPS


def get_processed_label(raw_label: str) -> str | None:
    reversed_raw_label = raw_label[::-1]

    try:
        return format(int(reversed_raw_label, 2), "03o")
    except ValueError:
        return None


def get_message_group(processed_label: str) -> str | None:
    return LABEL_GROUPS.get(processed_label)


def get_message_description(processed_label: str) -> str | None:
    return LABEL_DESCRIPTIONS.get(processed_label)
