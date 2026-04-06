from scripts.transform.config.label_config import MESSAGE_GROUPS


def get_processed_label(raw_label: str) -> str | None:
    reversed_raw_label = raw_label[::-1]

    try:
        return format(int(reversed_raw_label, 2), "03o")
    except ValueError:
        return None


def get_message_group(selected_message_group: str, processed_label: str) -> str | None:
    group_config = MESSAGE_GROUPS.get(selected_message_group)
    if group_config is None:
        return None

    if processed_label in group_config:
        return selected_message_group
    else:
        return None


def get_message_description(message_group: str, processed_label: str) -> str | None:
    label_config = MESSAGE_GROUPS[message_group].get(processed_label)
    if label_config is None:
        return None

    return label_config.get("description")
