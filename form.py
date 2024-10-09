from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField,StringField
from wtforms import validators
from wtforms.validators import DataRequired,Length


class infoForm(FlaskForm):
    patientname = StringField(
        "Name of Patient",
        validators=[DataRequired(),Length(2,30)]
    )
    image = FileField('Upload MRI Image',validators=[DataRequired()])
    submit = SubmitField("Result")