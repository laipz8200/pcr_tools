from flask import redirect, render_template, url_for
import hashlib

from app.main import bp
from app.main.forms import IconForm
from app.models import Icon
from app.utils import processer, structure
from app.utils.name2id import id2name, name2id


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/create_icon/<icon_id>', methods=['GET', 'POST'])
def create_icon(icon_id=None):
    form = IconForm()
    """
    这里根据 icon_id 从 db 获取 base64 值和 name
    :icon_id: md5 for icon
    :name: character's name
    """
    if icon_id is not None:
        icon = Icon.query.filter_by(icon_id=icon_id).first()
        if icon:
            icon_data = icon.base64.decode('utf-8')
            name = icon.name
    else:
        icon_data = None
        name = None

    if form.validate_on_submit():
        c_id = name2id(form.name.data)
        c_name = id2name(c_id)

        character = structure.Character(name=c_name, id=c_id, stars=form.stars.data,
                              ranks=form.ranks.data, has_equip=form.has_equip.data)
        sequence = f"{character.id}{character.stars}{character.ranks}" + ('E' if character.has_equip else '')
        icon_id = hashlib.md5(sequence.encode('utf-8')).hexdigest()

        icon = Icon.query.filter_by(icon_id=icon_id).first()
        if icon is None:
            icon_id = processer.create_icon(character)

        return redirect(url_for('main.create_icon', icon_id=icon_id))
    return render_template(
        'create_icon.html',
        title='角色图标生成',
        form=form,
        icon=icon_data,
        name=name,
    )
