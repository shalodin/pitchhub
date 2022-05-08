from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    """ 
    class modelling the users 
    """
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Pitch", backref="user", lazy="dynamic")
    comment = db.relationship("Comments", backref="user", lazy="dynamic")
    

  
    @property
    def password(self):
        raise AttributeError("You cant always get it right")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'User {self.username}'
    



class Pitch(db.Model):
    """
    List of pitches  
    """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id")) 
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    comment = db.relationship('Comments', backref='pitch', lazy="dynamic")




    # all_pitches=[]
    # def __init__(self,pitch_id,pitch_title,postedOn):
    #     self.pitch_id=pitch_id
    #     self.pitch_title=pitch_title
    #     self.postedOn=postedOn
        
        
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


    
    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(pitch_category=category).all()
        return pitches

    @classmethod
    def getPitchId(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    def save_vote(self: likes):
        db.session.add(self)
        db.session.commit()
 
class Comments(db.Model):
    """
    comment model for each pitch 
    """
    __tablename__ = 'comments'

    # add columns
    id = db.Column(db.Integer, primary_key=True)
    opinion = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment




            

   
