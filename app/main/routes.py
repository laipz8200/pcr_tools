import os
from flask import render_template, request, url_for, redirect, send_from_directory
from app.main import bp
from app.main.forms import IconForm
from app.utils.genicon import genicon
from app.utils.name2id import name2id


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/<img_name>', methods=['GET', 'POST'])
def index(img_name=None):
    if not img_name:
        img_name = 'unknow'
    form = IconForm()
    if form.validate_on_submit():
        name = form.name.data
        star = form.star.data
        rank = form.rank.data
        equip = form.equip.data

        c_id = name2id(name)
        print(name, star,rank, equip, c_id)
        if not os.path.exists(f'app/static/icons/{star}X_R{rank}_{c_id}{"E" if equip else ""}.png'):
            try:
                img = genicon(name, star, rank, equip)
                img.save(f'app/static/icons/{star}X_R{rank}_{c_id}{"E" if equip else ""}.png', 'PNG')
                img_name = f'{star}X_R{rank}_{c_id}{"E" if equip else ""}'
            except FileNotFoundError:
                img_name = 'unknow'
        else:
            img_name = f'{star}X_R{rank}_{c_id}{"E" if equip else ""}'
        return redirect(url_for('main.index', img_name=img_name))
    return render_template(
        'form.html',
        title='角色图标生成',
        form=form,
        img=img_name+'.png'
    )
