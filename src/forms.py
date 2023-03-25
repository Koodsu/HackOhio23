from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectMultipleField, RadioField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired
from flask_simplelogin import is_logged_in

forms_blueprint = Blueprint('forms', __name__, template_folder='templates')

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
    other = StringField('Tell us about you!')

@forms_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    if not is_logged_in():
        return redirect(url_for('simplelogin.login'))

    form = InformationForm()
    if form.validate_on_submit():
        data = [form.age.data, form.gender.data, form.hobbies.data, form.occupation.data, form.other.data]
        data = [i for i in data if i is not None]
        print(data)
        todolist = ["sussy", "hello", "among us"]
        return render_template('stuff.html', data=todolist)
    return render_template('forms.html', form=form)