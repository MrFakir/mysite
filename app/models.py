from app import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)

    more_info = db.relationship('MoreInfo', backref='categories', uselist=False)
    posts_list = db.relationship('Posts', backref='categories')


class StartPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(100), default='Click here!')
    url_video = db.Column(db.String(100))
    url_image = db.Column(db.String(100))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    #
    # def __repr__(self):
    #     return f'<users {self.id}>'


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.Text())
    button_name = db.Column(db.String(15))
    button_url = db.Column(db.String(100))
    image = db.Column(db.String(100))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    # def __repr__(self):
    #     return f'<users {self.id}>'


class MoreInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.Text())

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    #
    # def __repr__(self):
    #     return f'<users {self.id}>'
