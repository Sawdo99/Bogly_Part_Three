"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://img.icons8.com/?size=100&id=7819&format=png&color=000000"


# MODELS --------------------------------------------------------------------------
class User(db.Model):
   
    __tablename__ = "Users"

    id = db.Column(db.Integar, primary_key=True, autoincrement=True)
    first_name = db.Column(db.text, nullable=False)
    last_name = db.Column(db.text, nullable=False)
    image_url = db.Column(db.text, nullable=False, default=DEFAULT_IMAGE_URL)

    post = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """returns user name"""
        return f"{self.first_name} {self.last_name}"

    class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

    def connect_db(app):
        """Connects to db"""

        db.app = app
        db.init_app(app)

class Tag(db.Model):
    """Tag that can be added to posts."""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship(
        'Post',
        secondary="posts_tags",
        # cascade="all,delete",
        backref="tags",
    )


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


