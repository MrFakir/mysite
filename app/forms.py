from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactsForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(),
                                          Length(min=2, max=50, message='Длинна имени должна быть 2-50 символов')])
    email = StringField('Email', validators=[DataRequired(), Email('Не правильный формат Email')])
    messages = TextAreaField('Текст', validators=[
        DataRequired(), Length(min=0, max=1000, message='Максимальная длинна сообщения 1000 символов')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Отправить')

#