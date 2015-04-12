from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
class Graph(Form):
    x_cor = TextField("Enter x coordinates")
    y_cor = TextField("Enter y coordinates")
    submit = SubmitField("PlotTheGraph")