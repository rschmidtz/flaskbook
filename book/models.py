from book import db,bcrypt
from hashlib import md5


# low level APIs flask-sqlalchemy
followers = db.Table('followers',
    db.Column('follower_id',db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id',db.Integer, db.ForeignKey('user.id'))
    )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(60))
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(110), unique=True)
    password = db.Column(db.String(80))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    phone = db.Column(db.String(20))
    location = db.Column(db.String(50))
    website = db.Column(db.String(50))

    posts = db.relationship('Post',backref="author",lazy='dynamic')

    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')

    def __init__(self,fullname,username,email,password):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


    def __repr__(self):
        return '<User %r>' %self.username

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self,user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self,user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0


    def followed_posts(self):
        return Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter
        (followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,body,timestamp,user_id):
        self.body = body
        self.timestamp = timestamp
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % (self.body)
