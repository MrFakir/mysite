import os
import psw

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = psw.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.mail.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = psw.MAIL_USERNAME  # введите свой адрес электронной почты здесь
    MAIL_DEFAULT_SENDER = psw.MAIL_DEFAULT_SENDER  # и здесь
    MAIL_PASSWORD = psw.MAIL_PASSWORD  # введите пароль

    RECAPTCHA_PUBLIC_KEY = psw.RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PRIVATE_KEY = psw.RECAPTCHA_PRIVATE_KEY
