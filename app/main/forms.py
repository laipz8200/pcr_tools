from flask_wtf import FlaskForm
from wtforms import (BooleanField, IntegerField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, NumberRange


class IconForm(FlaskForm):
    name = StringField('角色', validators=[DataRequired()])
    # star = IntegerField('星级', validators=[DataRequired(), NumberRange(1, 6, '星级必须为1-6之间的整数')])
    stars = SelectField(
        '星级',
        choices=[(1, '1⭑'), (2, '2⭑'), (3, '3⭑'), (4, '4⭑'), (5, '5⭑'), (6, '6⭑')],
        default=(1, '1⭑'),
        coerce=int
    )
    ranks = IntegerField('Rank', validators=[NumberRange(0, 17, 'rank必须为1-17之间的整数, 填0不显示rank')], default=0)
    has_equip = BooleanField('专武')
    submit = SubmitField('生成')
