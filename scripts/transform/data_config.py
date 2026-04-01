from typing import TypedDict


class FieldConfig(TypedDict):
    start_pos: int
    end_pos: int
    min_val: float
    max_val: float


DATA_CONFIG: dict[str, dict[str, FieldConfig]] = {
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
    # PNK (12A)
    "340": {
        "value": {
            "start_pos": 2,
            "end_pos": 20,
            "min_val": 0,
            "max_val": 6000,
        }
    },
    # PNK (18A)
    "224": {
        "value": {
            "start_pos": 2,
            "end_pos": 17,
            "min_val": 0,
            "max_val": 30000,
        }
    },
    "226": {
        "value": {
            "start_pos": 2,
            "end_pos": 17,
            "min_val": 150,
            "max_val": 1600,
        }
    },
    "225": {
        "value": {
            "start_pos": 2,
            "end_pos": 17,
            "min_val": 0.3,
            "max_val": 3.5,
        }
    },
    # PNK (20A)
    "212": {
        "value": {
            "start_pos": 0,
            "end_pos": 17,
            "min_val": 0,
            "max_val": 2500,
        }
    },
    # PNK (21A)
    "241": {
        "value": {
            "start_pos": 0,
            "end_pos": 17,
            "min_val": -90,
            "max_val": 90,
        }
    },
    "242": {
        "value": {
            "start_pos": 0,
            "end_pos": 17,
            "min_val": -180,
            "max_val": 180,
        }
    },
    "272": {
        "value": {
            "start_pos": 2,
            "end_pos": 17,
            "min_val": 0,
            "max_val": 20000,
        }
    },
    # PNK (25A)
    "370": {
        "value": {
            "start_pos": 0,
            "end_pos": 17,
            "min_val": -10,
            "max_val": 45,
        }
    },
    "322": {
        "value": {
            "start_pos": 2,
            "end_pos": 17,
            "min_val": 5,
            "max_val": 40,
        }
    },
    "323": {
        "value": {
            "start_pos": 0,
            "end_pos": 17,
            "min_val": -10,
            "max_val": 5,
        }
    },
}
