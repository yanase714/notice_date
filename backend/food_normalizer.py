# 仮作成

NORMALIZE_MAP = {
    "milk": "牛乳",
    "MILK": "牛乳",
    "低脂肪乳": "牛乳",

    "egg": "卵",
    "EGG": "卵",
    "たまご": "卵",
    "玉子": "卵",

    "ヨーグルト": "ヨーグルト",
    "yogurt": "ヨーグルト",
}


def normalize_food(name: str) -> str:
    """
    食材名を統一する
    """
    key = name.strip().lower()
    return NORMALIZE_MAP.get(key, name)