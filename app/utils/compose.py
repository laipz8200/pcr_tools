import os
import numpy as np
from PIL import Image, ImageFont, ImageDraw


def create_icon(character_id: int, star_nu: int=1, has_equip: bool=False, rank: int=0):
    """
    合成角色图标
    """
    # Star坐标集
    coordinates_star = [(3, 105), (23, 105), (43, 105), (63, 105), (83, 105), (103, 105)]

    if star_nu < 3:
        character_star = 1
    elif 3 <= star_nu < 6:
        character_star = 3
    else:
        character_star = 6

    if not os.path.exists(f'res/character/icon_unit_{character_id}{character_star}1.png') and character_star == 6:
        raise FileNotFoundError('this character have not 6 star')
    character = Image.open(f'res/character/icon_unit_{character_id}{character_star}1.png').resize((128, 128))
    star = Image.open('res/icon/star.png').resize((20, 20))
    star_disabled = Image.open('res/icon/star_disabled.png').resize((20, 20))

    pt = iter(coordinates_star)
    try:
        for _ in range(star_nu):
            character.alpha_composite(star, next(pt))
        for _ in range(star_nu, 5):
            character.alpha_composite(star_disabled, next(pt))
    except StopIteration:
        pass

    if star_nu >= 6:
        # 加载粉色星星
        star_pink = Image.open('res/icon/star_pink.png').resize((20, 20))
        character.alpha_composite(star_pink, coordinates_star[-1])
    if 0 < rank <= 17:
        # 设置Rank标志坐标
        coordinates_rank = (33, 0)
        # 设置字体、颜色
        text_font = ImageFont.truetype('res/font/WenQuanYiMicroHei-01.ttf', 25)
        text_color = (0, 0, 0)
        # 添加遮罩
        mask = Image.new('RGBA', (128, 30), (255, 255, 255, 100))
        character.paste(mask, (0, 0), mask.convert('RGBA'))

        # 添加Rank文字
        draw = ImageDraw.Draw(character)
        font_x, font_y = coordinates_rank
        draw.text(coordinates_rank, f'Rank {rank}', text_color, text_font)
        draw.text((font_x+1, font_y+1), f'Rank {rank}', text_color, text_font)
    if has_equip:
        # 设置专武标志坐标
        coordinates_equip = (3, 3)
        # 加载专武图标
        equip = Image.open('res/icon/equip.png').resize((26, 26))
        character.alpha_composite(equip, coordinates_equip)
    
    return character


def create_team():
    pass