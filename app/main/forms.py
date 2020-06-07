from flask_wtf import FlaskForm
from wtforms import (BooleanField, IntegerField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, NumberRange


class IconForm(FlaskForm):
    name = StringField('角色', validators=[DataRequired()])
    stars = SelectField(
        '星级',
        choices=[(1, '1⭑'), (2, '2⭑'), (3, '3⭑'), (4, '4⭑'), (5, '5⭑'), (6, '6⭑')],
        default=(1, '1⭑'),
        coerce=int
    )
    ranks = IntegerField('Rank', validators=[NumberRange(0, 17, 'rank必须为1-17之间的整数, 填0不显示rank')], default=0)
    has_equip = BooleanField('专武')
    submit = SubmitField('生成')


class TeamForm(FlaskForm):
    name1 = StringField('角色1', validators=[DataRequired()])
    name2 = StringField('角色2', validators=[DataRequired()])
    name3 = StringField('角色3', validators=[DataRequired()])
    name4 = StringField('角色4', validators=[DataRequired()])
    name5 = StringField('角色5', validators=[DataRequired()])
    submit = SubmitField('生成')