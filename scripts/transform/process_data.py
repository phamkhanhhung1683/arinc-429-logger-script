from decimal import Decimal, getcontext
import json

getcontext().prec = 40


def get_processed_data(label: str, raw_data: str) -> str | None:
    LABEL_CONFIG: dict[str, dict[str, dict[str, float | int]]] = {
        # test
        # "030": {
        #     "value": {
        #         "start_pos": 9,
        #         "end_pos": 17,
        #         "min_val": -45,
        #         "max_val": 45,
        #     }
        # },
        # A-737
        "210": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 180,
            },
        },
        "211": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 180,
            },
        },
        "223": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 131072,
            },
        },
        "266": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 6068.6336,
            },
        },
        "267": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 6068.6336,
            },
        },
        "264": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 6068.6336,
            },
        },
        "324": {
            "gio": {
                "start_pos": 3,
                "end_pos": 8,
                "min_val": 0,
                "max_val": 32,
            },
            "phut": {
                "start_pos": 8,
                "end_pos": 14,
                "min_val": 0,
                "max_val": 64,
            },
            "giay": {
                "start_pos": 14,
                "end_pos": 20,
                "min_val": 0,
                "max_val": 64,
            },
        },
        "127": {
            "value": {
                "start_pos": 2,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 209715.2,
            },
        },
        "320": {
            "value": {
                "start_pos": 2,
                "end_pos": 17,
                "min_val": 0,
                "max_val": 32768,
            },
        },
        # Kh-31A
        "141": {
            "value": {
                "start_pos": 5,
                "end_pos": 16,
                "min_val": 0,
                "max_val": 120,
            }
        },
        "154": {
            "value": {
                "start_pos": 6,
                "end_pos": 14,
                "min_val": 0,
                "max_val": 1.1,
            }
        },
        "156": {
            "value": {
                "start_pos": 6,
                "end_pos": 16,
                "min_val": -60,
                "max_val": -1,
            }
        },
        "150": {
            "value": {
                "start_pos": 9,
                "end_pos": 17,
                "min_val": -45,
                "max_val": 45,
            }
        },
        "151": {
            "value": {
                "start_pos": 9,
                "end_pos": 17,
                "min_val": -45,
                "max_val": 45,
            }
        },
    }

    configs = LABEL_CONFIG.get(label)
    if not configs:
        return None

    result: dict[str, str] = {}

    for name, cfg in LABEL_CONFIG[label].items():
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
