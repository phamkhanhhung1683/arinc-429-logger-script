MESSAGE_GROUPS = {
    "A-737": {
        "317": {
            "description": "Từ nhận dạng",
        },
        "210": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "211": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 180,
                },
            ],
        },
        "010": {
            "description": "Vĩ độ mở rộng / kinh độ mở rộng",
            "fields": [
                {
                    "name": "vi_do_mo_rong",
                    "start_pos": 2,
                    "end_pos": 12,
                    "min_val": 0,
                    "max_val": 0.000086,
                },
                {
                    "name": "kinh_do_mo_rong",
                    "start_pos": 12,
                    "end_pos": 22,
                    "min_val": 0,
                    "max_val": 0.000086,
                },
            ],
        },
        "223": {
            "description": "Độ cao của anten vệ tinh so với mực nước biển (m)",
            "fields": [
                {
                    "name": "do_cao_cua_anten_ve_tinh_so_voi_muc_nuoc_bien",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 131072,
                },
            ],
        },
        "266": {
            "description": "Vận tốc theo hướng bắc (km/h)",
            "fields": [
                {
                    "name": "van_toc_theo_huong_bac",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 6068.6336,
                },
            ],
        },
        "267": {
            "description": "Vận tốc theo phương đông (km/h)",
            "fields": [
                {
                    "name": "van_toc_theo_huong_dong",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 6068.6336,
                },
            ]
        },
        "264": {
            "description": "Vận tốc theo hướng thẳng (km/h)",
            "fields": [
                {
                    "name": "van_toc_theo_huong_thang",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 6068.6336,
                },
            ],
        },
        "324": {
            "description": "Thời gian ghi dữ liệu (giờ - phút - giây)",
            "fields": [
                {
                    "name": "gio",
                    "start_pos": 3,
                    "end_pos": 8,
                    "min_val": 0,
                    "max_val": 32,
                },
                {
                    "name": "phut",
                    "start_pos": 8,
                    "end_pos": 14,
                    "min_val": 0,
                    "max_val": 64,
                },
                {
                    "name": "giay",
                    "start_pos": 14,
                    "end_pos": 20,
                    "min_val": 0,
                    "max_val": 64,
                },
            ],
        },
        "127": {
            "description": "Sai lệch thời gian (us)",
            "fields": [
                {
                    "name": "sai_lech_thoi_gian",
                    "start_pos": 2,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 209715.2,
                },
            ],
        },
        "320": {
            "description": "Sai số vị trí ước tính (m)",
            "fields": [
                {
                    "name": "sai_lech_vi_tri_uoc_tinh",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 32768,
                },
            ],
        },
        "126": {
            "description": "Thời gian (năm - tháng - ngày)",
            "fields": [
                {
                    "name": "nam",
                    "start_pos": 3,
                    "end_pos": 10,
                    "min_val": 0,
                    "max_val": 128,
                },
                {
                    "name": "thang",
                    "start_pos": 10,
                    "end_pos": 14,
                    "min_val": 0,
                    "max_val": 16,
                },
                {
                    "name": "ngay",
                    "start_pos": 14,
                    "end_pos": 19,
                    "min_val": 0,
                    "max_val": 32,
                },
            ],
        },
        "031": {
            "description": "Loại vệ tinh (số hiệu vị trí - hệ số suy hao - số lượng vệ tinh)",
            "fields": [
                {
                    "name": "so_hieu_vi_tri",
                    "start_pos": 3,
                    "end_pos": 9,
                    "min_val": 0,
                    "max_val": 64,
                },
                {
                    "name": "he_so_suy_hao",
                    "start_pos": 9,
                    "end_pos": 19,
                    "min_val": 0,
                    "max_val": 102.4,
                },
                {
                    "name": "so_luong_ve_tinh",
                    "start_pos": 19,
                    "end_pos": 23,
                    "min_val": 0,
                    "max_val": 16,
                },
            ],
        },
        "030": {
            "description": "Số lượng vệ tinh - tỷ số tín trên tạp - số kênh thu",
            "fields": [
                {
                    "name": "so_luong_ve_tinh",
                    "start_pos": 3,
                    "end_pos": 7,
                    "min_val": 0,
                    "max_val": 16,
                },
                {
                    "name": "ty_so_tin_tren_tap",
                    "start_pos": 7,
                    "end_pos": 15,
                    "min_val": 0,
                    "max_val": 25.6,
                },
                {
                    "name": "so_kenh_thu",
                    "start_pos": 15,
                    "end_pos": 19,
                    "min_val": 0,
                    "max_val": 16,
                },
            ],
        },
        "377": {
            "description": "Góc phương vị - góc ngẩng",
            "fields": [
                {
                    "name": "goc_phuong_vi",
                    "start_pos": 2,
                    "end_pos": 11,
                    "min_val": 0,
                    "max_val": 360,
                },
                {
                    "name": "goc_ngang",
                    "start_pos": 11,
                    "end_pos": 18,
                    "min_val": 0,
                    "max_val": 90,
                },
            ],
        },
        "153": {
            "description": "Mã phiên bản phần mềm (năm - tháng - lĩnh vực - loại phần mềm - mã số PMO)",
        },
    },
    "Kh-31A (3B, 4B)": {
        "157": {
            "description": "Từ mã kiểm tra",
        },
        "141": {
            "description": "Cự ly",
            "fields": [
                {
                    "name": "cu_ly",
                    "start_pos": 5,
                    "end_pos": 16,
                    "min_val": 0,
                    "max_val": 120,
                },
            ],
        },
        "154": {
            "description": "Tốc độ tiếp cận",
            "fields": [
                {
                    "name": "toc_do_tiep_can",
                    "start_pos": 6,
                    "end_pos": 14,
                    "min_val": 0,
                    "max_val": 1.1,
                },
            ],
        },
        "156": {
            "description": "Cự ly kích hoạt",
            "fields": [
                {
                    "name": "cu_ly_kich_hoat",
                    "start_pos": 6,
                    "end_pos": 16,
                    "min_val": -60,
                    "max_val": -1,
                },
            ],
        },
        "150": {
            "description": "Góc nghiêng",
            "fields": [
                {
                    "name": "goc_nghieng",
                    "start_pos": 9,
                    "end_pos": 17,
                    "min_val": -45,
                    "max_val": 45,
                },
            ],
        },
        "151": {
            "description": "Góc ngẩng",
            "fields": [
                {
                    "name": "goc_ngang",
                    "start_pos": 9,
                    "end_pos": 17,
                    "min_val": -45,
                    "max_val": 45,
                },
            ],
        },
        "155": {
            "description": "Lệnh đơn",
        },
        "201": {
            "description": "Từ mã SUO",
        },
    },
    "PNK (5A)": {
        "331": {
            "description": "Góc nghiêng tanga hiện tại - pitch",
            "fields": [
                {
                    "name": "goc_nghieng_tanga_hien_tai",
                    "start_pos": 0,
                    "end_pos": 15,
                    "min_val": -90,
                    "max_val": 90,
                },
            ],
        },
        "330": {
            "description": "Góc nghiêng kren hiện tại - roll",
            "fields": [
                {
                    "name": "goc_nghieng_kren_hien_tai",
                    "start_pos": 0,
                    "end_pos": 15,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "277": {
            "description": "Khóa la bàn từ tính (con quay hồi chuyển)",
            "fields": [
                {
                    "name": "khoa_la_ban_tu_tinh",
                    "start_pos": 0,
                    "end_pos": 10,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "273": {
            "description": "Bản tin 10",
            "fields": [
                {
                    "name": "ban_tin_10",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
    },
    "PNK (12A)": {
        "340": {
            "description": "Chiều cao hình học",
            "fields": [
                {
                    "name": "chieu_cao_hinh_hoc",
                    "start_pos": 2,
                    "end_pos": 20,
                    "min_val": 0,
                    "max_val": 6000,
                },
            ],
        },
    },
    "PNK (18A)": {
        "223": {
            "description": "Độ cao tuyệt đối theo áp suất",
            "fields": [
                {
                    "name": "do_cao_tuyet_doi_theo_ap_suat",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -500,
                    "max_val": 30000,
                },
            ],
        },
        "224": {
            "description": "Độ cao tương đối theo áp suất",
            "fields": [
                {
                    "name": "do_cao_tuong_doi_theo_ap_suat",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 30000,
                },
            ],
        },
        "226": {
            "description": "Vận tốc chỉ thị",
            "fields": [
                {
                    "name": "van_toc_chi_thi",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 150,
                    "max_val": 1600,
                },
            ],
        },
        "230": {
            "description": "Vận tốc không khí thực",
            "fields": [
                {
                    "name": "van_toc_khong_khi_thuc",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 150,
                    "max_val": 3500,
                },
            ],
        },
        "225": {
            "description": "Số mach hiện tại",
            "fields": [
                {
                    "name": "so_mach_hien_tai",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0.3,
                    "max_val": 3.5,
                },
            ],
        },
        "221": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 1000,
                },
            ],
        },
    },
    "PNK (20A)": {
        "211": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "210": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -90,
                    "max_val": 90,
                },
            ],
        },
        "266": {
            "description": "Vận tốc thành phần",
            "fields": [
                {
                    "name": "van_toc_thanh_phan",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -2500,
                    "max_val": 2500,
                },
            ],
        },
        "212": {
            "description": "Vận tốc hành trình",
            "fields": [
                {
                    "name": "van_toc_hanh_trinh",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 2500,
                },
            ],
        },
        "376": {
            "description": "Lệnh đơn",
        },
        "214": {
            "description": "Hướng bay thực tế",
            "fields": [
                {
                    "name": "huong_bay_thuc_te",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
    },
    "PNK (21A)": {
        "000": {
            "description": "Dự phòng",
        },
        "240": {
            "description": "Dấu hiệu",
        },
        "241": {
            "description": "Vĩ độ",
            "fields": [
                {
                    "name": "vi_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -90,
                    "max_val": 90,
                },
            ],
        },
        "242": {
            "description": "Kinh độ",
            "fields": [
                {
                    "name": "kinh_do",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "204": {
            "description": "Hướng bay thực tế",
            "fields": [
                {
                    "name": "huong_bay_thuc_te",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "272": {
            "description": "Tầm bay còn lại theo nhiên liệu",
            "fields": [
                {
                    "name": "tam_bay_con_lai_theo_nhien_lieu",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0,
                    "max_val": 20000,
                },
            ],
        },
    },
    "PNK (25A)": {
        "370": {
            "description": "Góc tấn công",
            "fields": [
                {
                    "name": "goc_tan_cong",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -10,
                    "max_val": 45,
                },
            ],
        },
        "322": {
            "description": "Góc tấn công tối đa cho phép",
            "fields": [
                {
                    "name": "goc_tan_cong_toi_da_cho_phep",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 5,
                    "max_val": 40,
                },
            ],
        },
        "323": {
            "description": "Góc tấn công tối thiểu",
            "fields": [
                {
                    "name": "goc_tan_cong_toi_thieu",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -10,
                    "max_val": 5,
                },
            ],
        },
        "371": {},
        "346": {
            "description": "Bản tin 14",
            "fields": [
                {
                    "name": "ban_tin_14",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -4,
                    "max_val": 10,
                },
            ],
        },
        "333": {},
        "326": {},
        "327": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 17,
                    "min_val": -4,
                    "max_val": 1.5,
                },
            ],
        },
        "227": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 500,
                    "max_val": 1800,
                },
            ],
        },
        "321": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 200,
                    "max_val": 500,
                },
            ],
        },
        "373": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 2,
                    "end_pos": 17,
                    "min_val": 0.7,
                    "max_val": 3,
                },
            ],
        },
    },
    "PNK (11B, 41A)": {
        "332": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 16,
                    "min_val": -80,
                    "max_val": 80,
                },
            ],
        },
        "346": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 16,
                    "min_val": -0.2,
                    "max_val": 5,
                },
            ],
        },
        "376": {},
        "214": {
            "fields": [
                {
                    "name": "?",
                    "start_pos": 0,
                    "end_pos": 18,
                    "min_val": -180,
                    "max_val": 180,
                },
            ],
        },
        "221": {},
        "230": {},
    },
    # "SUO (9A)": {
    #     "241",
    #     "242",
    #     "243",
    #     "244",
    #     "245",
    #     "246",
    #     "247",
    #     "250",
    #     "251",
    #     "252",
    # },
    # "SUO (LS1)": {
    #     "215",
    #     "216",
    #     "217",
    #     "220",
    #     "222",
    #     "231",
    #     "232",
    #     "223",
    #     "210",
    #     "211",
    #     "221",
    #     "230",
    #     "214",
    #     "224",
    #     "225",
    #     "233",
    #     "226",
    #     "242",
    #     "240",
    #     "227",
    #     "245",
    # },
    # "SUO (LS3)": {
    #     "320",
    #     "323",
    #     "324",
    #     "325",
    #     "326",
    #     "327",
    #     "330",
    #     "331",
    #     "332",
    #     "340",
    #     "341",
    #     "342",
    #     "343",
    #     "344",
    #     "345",
    #     "346",
    #     "347",
    #     "350",
    #     "351",
    #     "352",
    # },
}
