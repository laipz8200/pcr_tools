import os
from PIL import Image
from app.utils.name2id import name2id
from app.utils.compose import compose


def genicon(name: str, star: int, rank: int=0, has_equip :bool=False):
    c_id = name2id(name)
    if c_id == 1000:
        raise FileNotFoundError
    else:
        try:
            img = compose(c_id, star, has_equip, rank)
        except Exception:
            raise
    return img
