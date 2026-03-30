def process_label(raw_label: str) -> str | None:
    reversed_raw_label = raw_label[::-1]

    try:
        return format(int(reversed_raw_label, 2), "03o")
    except ValueError:
        return None


def get_message_group(processed_label: str) -> str | None:
    LABEL_MAP = {
        "317": "A-737",
        "210": "A-737",
        "211": "A-737",
        "010": "A-737",
        "223": "A-737",
        "266": "A-737",
        "267": "A-737",
        "264": "A-737",
        "324": "A-737",
        "127": "A-737",
        "320": "A-737",
        "126": "A-737",
        "031": "A-737",
        "030": "A-737",
        "377": "A-737",

        "157": "Kh-31A (3B, 4B)",
        "141": "Kh-31A (3B, 4B)",
        "154": "Kh-31A (3B, 4B)",
        "156": "Kh-31A (3B, 4B)",
        "152": "Kh-31A (3B, 4B)",
        "150": "Kh-31A (3B, 4B)",
        "151": "Kh-31A (3B, 4B)",
        "155": "Kh-31A (3B, 4B)",
        "201": "Kh-31A (3B, 4B)",

        "153": "A-737 / Kh-31A (3B, 4B)",
    }

    return LABEL_MAP.get(processed_label)


def get_message_description(processed_label: str) -> str | None:
    LABEL_DESCRIPTIONS = {
        # A-737
        "317": "Từ nhận dạng",
        "210": "Vĩ độ (độ)",
        "211": "Kinh độ (độ)",
        "010": "Vĩ độ mở rộng / kinh độ mở rộng",
        "223": "Độ cao của anten vệ tinh so với mực nước biển",
        "266": "Vận tốc theo hướng bắc",
        "267": "Vận tốc theo phương đông",
        "264": "Vận tốc theo hướng thẳng",
        "324": "Thời gian ghi dữ liệu (giờ - phút - giây)",
        "127": "Sai lệch thời gian",
        "320": "Sai số vị trí ước tính",
        "126": "Date (năm - tháng - ngày)",
        "031": "Loại vệ tinh (số hiệu vị trí - hệ số suy hao - số lượng vệ tinh)",
        "030": "Số lượng vệ tinh - tỷ số tín trên tạp - số kênh thu",
        "377": "Góc phương vị - góc ngẩng",
        # Kh-31A
        "157": "Từ mã kiểm tra",
        "141": "Cự ly",
        "154": "Tốc độ tiếp cận",
        "156": "Cự ly kích hoạt",
        "152": "Góc tà / góc tà theo đường chân trời",
        "150": "Góc nghiêng",
        "151": "Góc ngẩng",
        "155": "Lệnh đơn",
        "201": "Từ mã SUO",
        # A-737 / Kh-31A
        "153": "Mã phiên bản phần mềm (năm - tháng - lĩnh vực - loại phần mềm - mã số PMO) (A-737) / góc phương vị (Kh-31A) / cự ly bổ nhào (Kh-31A)",
    }

    return LABEL_DESCRIPTIONS.get(processed_label)
