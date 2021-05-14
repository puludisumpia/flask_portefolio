from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField(label="votre nom".upper(), validators=[DataRequired()])
    email = StringField(label="votre mail".upper(), validators=[DataRequired()])
    phone = StringField(label="votre numéro télephone".upper(), validators=[DataRequired()])
    content = TextAreaField(label="votre message".upper(), validators=[DataRequired()])
    submit = SubmitField(label="Envoyer")