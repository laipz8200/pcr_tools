import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from app.utils.structure import Character


class ImageMaker(object):

    def create_icon(self, character: Character) -> Image:
        """
        合成角色图标
        """
        # Star坐标集
        coordinates_star = [(3, 105), (23, 105), (43, 105),
                            (63, 105), (83, 105), (103, 105)]

        lv = self._calc_lv(character.stars)

        if not os.path.exists(f"res/character/icon_unit_{character.id}{lv}1.png"):
            raise FileExistsError()
        icon = Image.open(
            f"res/character/icon_unit_{character.id}{lv}1.png").resize((128, 128))
        
        if character.id == 1000:
            return icon

        star = Image.open('res/icon/star.png').resize((20, 20))
        star_disabled = Image.open(
            'res/icon/star_disabled.png').resize((20, 20))

        pt = iter(coordinates_star)
        try:
            for _ in range(character.stars):
                icon.alpha_composite(star, next(pt))
            for _ in range(character.stars, 5):
                icon.alpha_composite(star_disabled, next(pt))
        except StopIteration:
            pass

        if character.stars >= 6:
            # 加载粉色星星
            star_pink = Image.open('res/icon/star_pink.png').resize((20, 20))
            icon.alpha_composite(star_pink, coordinates_star[-1])
        if 0 < character.ranks <= 17:
            # 设置Rank标志坐标
            coordinates_rank = (33, 0)
            # 设置字体、颜色
            text_font = ImageFont.truetype(
                'res/font/WenQuanYiMicroHei-01.ttf', 25)
            text_color = (0, 0, 0)
            # 添加遮罩
            mask = Image.new('RGBA', (128, 30), (255, 255, 255, 100))
            icon.paste(mask, (0, 0), mask.convert('RGBA'))

            # 添加Rank文字
            draw = ImageDraw.Draw(icon)
            font_x, font_y = coordinates_rank
            draw.text(coordinates_rank,
                      f"Rank {character.ranks}", text_color, text_font)
            draw.text((font_x+1, font_y+1),
                      f"Rank {character.ranks}", text_color, text_font)
        if character.has_equip:
            # 设置专武标志坐标
            coordinates_equip = (3, 3)
            # 加载专武图标
            equip = Image.open('res/icon/equip.png').resize((26, 26))
            icon.alpha_composite(equip, coordinates_equip)

        return icon

    def _calc_lv(self, stars):
        """
        计算星级所在的阶段
        1-2: 1 星
        3-5: 3 星
        6-6: 6 星
        """
        if stars < 3:
            return 1
        if 3 <= stars < 6:
            return 3
        return 6
