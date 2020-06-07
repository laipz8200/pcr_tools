from flask_wtf import FlaskForm
from wtforms import (BooleanField, IntegerField, SelectField, StringField,
                     SubmitField, FormField)
from wtforms.validators import DataRequired, NumberRange


class IconForm(FlaskForm):
    name = StringField('名字/昵称', validators=[DataRequired()])
    stars = SelectField(
        '星级',
        choices=[(1, '1⭑'), (2, '2⭑'), (3, '3⭑'),
                 (4, '4⭑'), (5, '5⭑'), (6, '6⭑')],
        default=(1, '1⭑'),
        coerce=int
    )
    ranks = IntegerField('Rank', validators=[NumberRange(
        0, 17, 'rank必须为1-17之间的整数, 填0不显示rank')], default=0)
    has_equip = BooleanField('专武')
    submit = SubmitField('生成')


class CharacterForm(FlaskForm):
    name = StringField('名字/昵称', validators=[DataRequired()], render_kw={'placeholder': '名字/昵称'})
    stars = SelectField(
        '星级',
        choices=[(1, '1⭑'), (2, '2⭑'), (3, '3⭑'),
                 (4, '4⭑'), (5, '5⭑'), (6, '6⭑')],
        default=(1, '1⭑'),
        coerce=int
    )
    ranks = IntegerField('Rank', validators=[NumberRange(
        0, 17, 'rank必须为1-17之间的整数, 填0不显示rank')], default=0)
    has_equip = BooleanField('专武')


class TeamForm(FlaskForm):
    character1 = FormField(CharacterForm, '角色1')
    character2 = FormField(CharacterForm, '角色2')
    character3 = FormField(CharacterForm, '角色3')
    character4 = FormField(CharacterForm, '角色4')
    character5 = FormField(CharacterForm, '角色5')
    submit = SubmitField('生成')
