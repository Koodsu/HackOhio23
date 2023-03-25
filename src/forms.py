from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectMultipleField, RadioField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired
from flask_simplelogin import login_required

forms_blueprint = Blueprint('forms', __name__, template_folder='templates')

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class InformationForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    gender = RadioField(choices=[
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 
        validators=[DataRequired()])
    hobbies = MultiCheckboxField(choices=[('sussy', 'huh'), ('baka', 'huh')])
    occupation = StringField('Tell us about your occupation!')
    other = StringField('Tell us about your other hobbies!')

@login_required(basic=True)
@forms_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    form = InformationForm()
    if form.validate_on_submit():
        data = [form.age.data, form.gender.data, form.hobbies.data, form.occupation.data, form.other.data]
        data = [i for i in data if i is not None]
        todolist = ["sussy", "hello", "among us"]
        return render_template('stuff.html', data=todolist)
    return render_template('forms.html', form=form)