from wtforms import Form, IntegerField, StringField, SelectField, PasswordField, validators


class SignInForm(Form):
    login = StringField(name='login', label='Login', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    password = PasswordField(name='password', label='Heslo', validators=[validators.InputRequired()])


class AddPhoneForm(Form):
    labour_intensity = IntegerField(name='labour_intensity', label='Pracovní náročnost', validators=[validators.InputRequired()])
    name = StringField(name='name', label='Jméno', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    type = IntegerField(name='type', label='Typ', validators=[validators.InputRequired()])
    processors_id_processor = SelectField('processors_id_processor', choices=[],id='select-field')
    cases_id_case = SelectField('cases_id_case', choices=[],id='select-field')
    batteries_id_battery = SelectField('batteries_id_battery', choices=[],id='select-field')
    user_id_employee = SelectField('user_id_employee', choices=[],id='select-field')
    img = StringField(name='img', label='Obrázek', validators=[validators.Length(min=2, max=2048)])
   

class AddUserForm(Form):
    login=StringField(name='login', label='login', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    password=StringField(name='password', label='password', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    user_type_id=SelectField('user_type_id', choices=[],id='select-field')
    name=StringField(name='name', label='name', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    surname=StringField(name='surname', label='surname', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    telephone =StringField(name='telephone', label='telephone', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    email=StringField(name='email', label='email', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    hourly_rate=IntegerField(name='hourly_rate', label='Hodinová sazba', validators=[validators.InputRequired()])

class EditUserForm(Form):
    login=StringField(name='login', label='login', validators=[validators.Length(min=2, max=30)])
    password=StringField(name='password', label='Heslo', validators=[validators.Length(min=2, max=30)])
    name=StringField(name='name', label='Jméno', validators=[validators.Length(min=2, max=30)])
    surname=StringField(name='surname', label='Příjmení', validators=[validators.Length(min=2, max=30)])
    telephone =StringField(name='telephone', label='Telefon', validators=[validators.Length(min=2, max=30)])
    email=StringField(name='email', label='E-mail', validators=[validators.Length(min=2, max=30)])

class DeleteUserForm(Form):
    id_user=IntegerField(name='id_user', label='Id uživatele', validators=[validators.InputRequired()])
