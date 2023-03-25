from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey("username"))
    email = db.Column(db.String, db.ForeignKey("email"))
    password = db.Column(db.String, db.ForeignKey("password"))

    def __repr__(self):
        return f"UserP'{self.id}', '{self.username}', '{self.email}', '{self.password}'"