import os

from flask import Flask, render_template
from forms import forms_blueprint
from register import register_blueprint
from models import db, User
from flask_simplelogin import SimpleLogin, login_required
from dotenv import load_dotenv
from cli import create_db, print_db, clear_db
import os

app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['FLASK_SIMPLELOGIN_URL'] = "/login"
app.config['FLASK_SIMPLELOGOUT_URL'] = "/logout"

app.cli.add_command(print_db)
app.cli.add_command(create_db)
app.cli.add_command(clear_db)

app.register_blueprint(register_blueprint)
app.register_blueprint(forms_blueprint)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, "tmp", "data.db")
db.init_app(app)

def login_checker(attempt):
    user = User.query.filter_by(username=attempt['username']).first()
    if user is not None and user.verify_password(attempt['password']):
        return True
    return False

simple_login = SimpleLogin(app, login_checker=login_checker)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/image')
def image():
    return render_template('image.html')
    
if __name__ == '__main__':
    app.run(debug=True)