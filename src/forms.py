from flask import Blueprint, render_template, redirect, url_for, Response
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectMultipleField, RadioField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired
from flask_simplelogin import is_logged_in

forms_blueprint = Blueprint('forms', __name__, template_folder='templates')
current_selection = None

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class InformationForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    gender = RadioField(choices=[
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 
        validators=[DataRequired()])
    hobbies = StringField('Hobbies')
    occupation = RadioField(choices=[('whitecolor', 'White Collar'), ('bluecolor', 'Blue Collar'), ('student', 'Student')])
    location = StringField('Location')
    other = StringField('Tell us about you!')

class TodoForm(FlaskForm):
    todos = MultiCheckboxField('Todos')

@forms_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    if not is_logged_in():
        return redirect(url_for('simplelogin.login'))

    form = InformationForm()
    if form.validate_on_submit():
        data = {
            'age': form.age.data,
            'gender': form.gender.data,
            'hobbies': form.hobbies.data,
            'occupation': form.occupation.data,
            'other': form.other.data,
            'location': form.location.data,
        }
        # run chatgpt to get todo
        form2 = TodoForm()
        choices = [('sussy', 'Sussy'), ('hello', 'Hello'), ('among us', 'Among Us')]
        current_selection = choices
        return analyze(choices)
    return render_template('forms.html', form=form)

@forms_blueprint.route('/analyze', methods=['POST'])
def analyze(choices=None):
    form = TodoForm()
    if choices is not None:
        form.todos.choices = choices
        return render_template('todo.html', form=form)
    else:
        non_selected = []
        for i in current_selection:
            if i[0] not in form.todos.data:
                non_selected.append(i[0])
        print("selected", form.todos.data)
        print("non selected", non_selected)
        return Response('Success', status=204)
    