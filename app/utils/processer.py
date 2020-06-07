import base64
import hashlib
from io import BytesIO

from PIL import Image

from app import db
from app.models import Icon
from app.utils.image_maker import ImageMaker
from app.utils.structure import Character


def create_icon(character: Character):
    maker = ImageMaker()
    try:
        image = maker.create_icon(character)
    except FileExistsError:
        character = Character(name='未知角色', id=1000, stars=3, ranks=0, has_equip=False)
        return create_icon(character)

    buffered = BytesIO()
    image.save(buffered, format='PNG')

    sequence = f"{character.id}{character.stars}{character.ranks}" + ('E' if character.has_equip else '')
    icon_id = hashlib.md5(sequence.encode('utf-8')).hexdigest()

    base64_value = base64.b64encode(buffered.getvalue())

    icon = Icon.query.filter_by(icon_id=icon_id).first()
    if icon is None:
        icon = Icon(icon_id=icon_id, name=character.name, base64=base64_value)
        db.session.add(icon)
        db.session.commit()
    return icon_id
