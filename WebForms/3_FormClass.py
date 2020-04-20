#each form is represented in server by a class that inherits from the class FlaskForm. 

#each field is represented by an object. 

#each field object has one or more validators attached. 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#this class inherits from parent FlaskForm
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
#the 'name' and 'submit' are both variables. And they are both assigned objects. 

#'StringField' class represents an HTML <input> element with a type = "text"

#SubmitField class represents an HTML <input> element with a type = "submit" attribute. 

#The first argument is the label that will be used when redering the form to HTML. 

#List of WTForms standard HTML fields are on the book table 4-1, and also a lot of validators. 
