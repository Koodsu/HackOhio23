from flask import Flask
from forms import forms_blueprint
from login import login_blueprint

app = Flask(__name__)

app.register_blueprint(forms_blueprint)
app.register_blueprint(login_blueprint)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)