from flask import Flask, render_template
from forms import forms_blueprint
from login import login_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfasdfwerqewgfgzvzxc'
app.register_blueprint(forms_blueprint)
app.register_blueprint(login_blueprint)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)