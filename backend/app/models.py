from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user_data'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    hpsw = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
