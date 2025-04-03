from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Follow(db.Model):
    __tablename__ = "follows"
    user_id = db.Column(db.String, db.ForeignKey("user.user_name"), primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.profile_id"), primary_key=True) 


class User(db.Model): 
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(60), unique = True, nullable = False)
    full_name = db.Column(db.String(100), nullable = False)
    user_name = db.Column(db.String(60), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    profile = db.relationship("Profile", backref=db.backref('User'))
    post = db.relationship("Post", backref=db.backref('User'))


class Profile(db.Model):
    __tablename__ = "profile"
    profile_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    about = db.Column(db.String(200))
    profile_pic = db.Column(db.String) 
    total_post = db.Column(db.Integer)
    user_id = db.Column(db.String, db.ForeignKey("user.user_name"), unique=True)


class Post(db.Model):
    __tablename__ = "post"
    post_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_name"))
    image = db.Column(db.String)
    heading = db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    # timestamp = db.Column(db.DateTime(timezone = True), default = datetime.now())
    timestamp=db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    __tablename__ = "comment"
    c_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.post_id") ) 
    comment = db.Column(db.String)

      

