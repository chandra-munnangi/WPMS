from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class WorkorderForm(FlaskForm):
    workorder_no = StringField('Workorder No', validators=[DataRequired()])
    workorder_date = DateField('Workorder Date', validators=[DataRequired()])
    item_name = SelectField('Item Name', validators=[DataRequired()])
    consignee = SelectField('Consignee', validators=[DataRequired()])
    allocation_no = StringField('Allocation No', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Create Workorder')

class ConsigneeForm(FlaskForm):
    zone = SelectField('Zone', validators=[DataRequired()])
    division = SelectField('Division', validators=[DataRequired()])
    indenter = StringField('Indenter', validators=[DataRequired()])
    consignee = StringField('Consignee', validators=[DataRequired()])
    consignee_type = SelectField('Consignee Type', choices=[('Home Revenue', 'Home Revenue'), ('Projects', 'Projects'), ('Construction', 'Construction')], validators=[DataRequired()])
    submit = SubmitField('Save Consignee')

class ItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_description = StringField('Item Description', validators=[DataRequired()])
    item_type = SelectField('Item Type', choices=[('SG', 'SG'), ('NSG', 'NSG')], validators=[DataRequired()])
    sg_number = StringField('SG Number')
    submit = SubmitField('Save Item')