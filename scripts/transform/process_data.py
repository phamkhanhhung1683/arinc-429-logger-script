from decimal import Decimal, getcontext
import json
from typing import TypedDict

getcontext().prec = 40


def get_processed_data(label: str, raw_data: str) -> str | None:
    class FieldConfig(TypedDict):
        start_pos: int
        end_pos: int
        min_val: float
        max_val: float

    LABEL_CONFIG: dict[str, dict[str, FieldConfig]] = {
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
        "010": {
            "vi_do_mo_rong": {
                "start_pos": 2,
                "end_pos": 12,
                "min_val": 0,
                "max_val": 0.000086,
            },
            "kinh_do_mo_rong": {
                "start_pos": 12,
                "end_pos": 22,
                "min_val": 0,
                "max_val": 0.000086,
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
        "126": {
            "nam": {
                "start_pos": 3,
                "end_pos": 10,
                "min_val": 0,
                "max_val": 128,
            },
            "thang": {
                "start_pos": 10,
                "end_pos": 14,
                "min_val": 0,
                "max_val": 16,
            },
            "ngay": {
                "start_pos": 14,
                "end_pos": 19,
                "min_val": 0,
                "max_val": 32,
            },
        },
        "031": {
            "so_hieu_vi_tri": {
                "start_pos": 3,
                "end_pos": 9,
                "min_val": 0,
                "max_val": 64,
            },
            "he_so_suy_hao": {
                "start_pos": 9,
                "end_pos": 19,
                "min_val": 0,
                "max_val": 102.4,
            },
            "so_luong_ve_tinh": {
                "start_pos": 19,
                "end_pos": 23,
                "min_val": 0,
                "max_val": 16,
            },
        },
        "030": {
            "so_luong_ve_tinh": {
                "start_pos": 3,
                "end_pos": 7,
                "min_val": 0,
                "max_val": 16,
            },
            "ty_so_tin_tren_tap": {
                "start_pos": 7,
                "end_pos": 15,
                "min_val": 0,
                "max_val": 25.6,
            },
            "so_kenh_thu": {
                "start_pos": 15,
                "end_pos": 19,
                "min_val": 0,
                "max_val": 16,
            },
        },
        "377": {
            "goc_phuong_vi": {
                "start_pos": 2,
                "end_pos": 11,
                "min_val": 0,
                "max_val": 360,
            },
            "goc_ngang": {
                "start_pos": 11,
                "end_pos": 18,
                "min_val": 0,
                "max_val": 90,
            },
        },
        # Kh-31A
        "141": {
            "value": {
                "start_pos": 5,
                "end_pos": 16,
                "min_val": 0,
                "max_val": 120,
            },
        },
        "154": {
            "value": {
                "start_pos": 6,
                "end_pos": 14,
                "min_val": 0,
                "max_val": 1.1,
            },
        },
        "156": {
            "value": {
                "start_pos": 6,
                "end_pos": 16,
                "min_val": -60,
                "max_val": -1,
            },
        },
        "150": {
            "value": {
                "start_pos": 9,
                "end_pos": 17,
                "min_val": -45,
                "max_val": 45,
            },
        },
        "151": {
            "value": {
                "start_pos": 9,
                "end_pos": 17,
                "min_val": -45,
                "max_val": 45,
            },
        },
        # PNK (5A)
        "331": {
            "value": {
                "start_pos": 0,
                "end_pos": 15,
                "min_val": -90,
                "max_val": 90,
            }
        },
        "330": {
            "value": {
                "start_pos": 0,
                "end_pos": 15,
                "min_val": -180,
                "max_val": 180,
            }
        },
        "277": {
            "value": {
                "start_pos": 0,
                "end_pos": 10,
                "min_val": -180,
                "max_val": 180,
            }
        },
        "273": {
            "value": {
                "start_pos": 0,
                "end_pos": 17,
                "min_val": -180,
                "max_val": 180,
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
