from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange


class IconForm(FlaskForm):
    name = StringField('角色', validators=[DataRequired()])
    # star = IntegerField('星级', validators=[DataRequired(), NumberRange(1, 6, '星级必须为1-6之间的整数')])
    star = SelectField(
        '星级',
        choices=[(1, '1⭑'), (2, '2⭑'), (3, '3⭑'), (4, '4⭑'), (5, '5⭑'), (6, '6⭑')],
        default=(1, '1⭑'),
        coerce=int
    )
    rank = IntegerField('Rank', validators=[NumberRange(0, 17, 'rank必须为1-17之间的整数, 填0不显示rank')])
    equip = BooleanField('专武')
    submit = SubmitField('生成')
