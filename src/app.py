import os

from flask import Flask, render_template
from forms import forms_blueprint
from login import login_blueprint
from models import db, User
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.register_blueprint(forms_blueprint)
app.register_blueprint(login_blueprint)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, "tmp", "data.db")
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()
    print("Database tables created")

#login_manager = LoginManager()
#login_manager.init_app(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)