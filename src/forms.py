from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired

forms_blueprint = Blueprint('forms', __name__, template_folder='templates')

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class InformationForm(FlaskForm):
    age = StringField('Name', validators=[DataRequired()])
    gender = MultiCheckboxField(choices=[
        ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 
        validators=[DataRequired()])
    hobbies = MultiCheckboxField(choices=[('sussy', 'huh'), ('baka', 'huh')])
    other = StringField('Tell us about your other hobbies!')
    submit = SubmitField('Submit')

@forms_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    form = InformationForm()
    if form.validate_on_submit():
        return 'Form submitted!'
    return render_template('forms.html', form=form)