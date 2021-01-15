from wtforms import  Form, SelectField, SubmitField

class UsersForm(Form):
    categories = SelectField("Categories: ", id="category", choices=[(0,"--Select Categories--")])
    submit = SubmitField("Submit")
