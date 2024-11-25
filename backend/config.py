class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/itam_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
