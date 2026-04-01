from decimal import Decimal, getcontext
import json

from scripts.transform.data_config import DATA_CONFIGS

getcontext().prec = 40


def get_processed_data(label: str, raw_data: str) -> str | None:
    configs = DATA_CONFIGS.get(label)
    if not configs:
        return None

    result: dict[str, str] = {}

    for name, cfg in DATA_CONFIGS[label].items():
        value = compute_data(
            raw_data,
            cfg["start_pos"],
            cfg["end_pos"],
            cfg["min_val"],
            cfg["max_val"],
        )

        if value is not None:
            result[name] = value

    if not result:
        return None

    return json.dumps(result, ensure_ascii=False)


def compute_data(
    binary_str: str, start_pos: int, end_pos: int, min_val: float, max_val: float
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

    return format(result, "f")
