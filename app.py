# Web applikation
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

def CalculateSalary(namn, timlon, hours):
    if namn.lower() == "stefan":
        timlon = timlon * 2
    return hours * timlon


app = Flask(__name__)
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

class SalaryForm(FlaskForm):
    name = StringField("Vad heter du?",validators=[DataRequired(),Length(min=4,
        message=('Minst 4 tecken tack ')
    )])
    hourlySalary = IntegerField('Timlön',  validators=[DataRequired()])
    hoursWorked = IntegerField('Timmar du jobbat',  validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route("/salary", methods=['GET', 'POST'])
def salary():
    form = SalaryForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        hoursWorked = int(form.hoursWorked.data)
        hourlySalary = int(form.hourlySalary.data)
        salary = CalculateSalary(name, hourlySalary, hoursWorked)
        message = f"Din lön är {salary}"
    #return render_template('nameage.html', form=form, message=message)    
    return render_template("salary.html", form=form, message=message)

   

@app.route("/hej.html")
def hej():
    return "Hejsan <b>på dig</b>"


@app.route("/")
def hello_world():
    return "<p>Hej <a href='/salary'>Kör lönekalkylatorn här!</a></p>"

app.run()    