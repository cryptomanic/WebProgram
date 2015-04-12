from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
class Average(Form):
    message = TextField("Enter space seperated numbers")
    submit = SubmitField("FindAverage")