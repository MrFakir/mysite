from threading import Thread

from flask import render_template, redirect, url_for, request, abort, flash
from app import app, mail
from app.forms import ContactsForm
from app.models import Categories
from flask_mail import Message


def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(title, name, email, message):
    msg = Message(f'Сообщение с моего сайта, раздел: {title}', sender='fakir_x@mail.ru',
                  recipients=['fakir_x@mail.ru', ])
    msg.body = f'Имя {name}, отправитель {email}, сообщение: {message}'
    msg.html = f'<b>Имя</b> {name}<br><b>Отправитель</b> {email}<br><b>Сообщение:</b><p>{message}</p>'
    thr = Thread(target=async_send_mail, args=[app, msg])
    thr.start()
    return thr


@app.route('/programmer', methods=['POST', 'GET'])
@app.route('/streamer', methods=['POST', 'GET'])
def show_category():
    title = request.path[1:]
    category_title = Categories.query.filter_by(title=title.lower()).one()
    more_info = category_title.more_info
    posts_list = category_title.posts_list
    for i, j in enumerate(posts_list):
        if i % 2 == 0:
            j.orient = 'left'
        else:
            j.orient = 'right'

    form = ContactsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            send_email(title=title, name=form.name.data, email=form.email.data, message=form.messages.data)
            flash('Сообщение отправлено, спасибо :)', category='success')
            return redirect(request.path+'#contact')
        else:
            flash('Сообщение не отправлено, проверьте правильность ввода', category='error')

    return render_template('one.html', title=title.capitalize(),
                           more_info=more_info, posts_list=posts_list, form=form)


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная страница')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title=error)


@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html', title=error)

