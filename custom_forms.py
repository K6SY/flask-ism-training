from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, FileField
from wtforms.validators import DataRequired, Email, InputRequired

class Newsletter(FlaskForm):
    name = StringField(label='Donnez votre nom?', validators=[DataRequired()]) 
    email = StringField(label='Merci d\'indiquer votre email?',validators=[InputRequired(), Email(message="Email invalide",check_deliverability=True)])
    mydate = DateField(label='Indiquer la date de souscription?', validators=[], format='%Y-%m-%d')
    submit = SubmitField('Submit')


class CategorieForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Submit')
