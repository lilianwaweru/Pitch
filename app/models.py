from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'users',lazy ="dynamic")
    comment = db.relationship('Comment',backref='users',lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    # users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'  

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(500))
    title = db.Column(db.String)
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comment = db.relationship('Comment',backref = 'pitches',lazy ="dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(id,category): 
        pitch = Pitch.query.filter_by(category = category).all()
        return pitch  

    @classmethod
    def get_all_pitches(cls):
       pitches = Pitch.query.order_by('id').all()
       return pitches

    @classmethod
    def get_category(cls,cat):
       category = Pitch.query.filter_by(pitch_category=cat).order_by('id').all()
       return category

    def __repr__(self):
        return f'Pitch {self.pitch_title}, {self.category}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(id,pitch):
        comment = Comment.query.filter_by(pitch_id = pitch).all()
        return comment

    def __repr__(self):
        return f'Comment{self.comment}'    