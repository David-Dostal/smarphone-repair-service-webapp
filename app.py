from flask import Flask, render_template, request, flash, redirect, url_for, session

import auth

from database import database
from service.part_service import PartService
from service.phone_service import PhoneService
from service.user_service import UserService
import forms

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
database.init_app(app)



@app.route("/")
def index():
    return render_template("index.jinja")


@app.route('/phones')
def view_products_page():
    phones = PhoneService.get_all()

    return render_template(
        "phones.jinja",
       phones = phones
    )

@app.route('/parts')
@auth.login_required
def view_parts_page():

    batteries = PartService.get_all_batteries()
    cases = PartService.get_all_cases()
    processors = PartService.get_all_processors()

    return render_template(
        "parts.jinja",
        batteries=batteries,
        cases=cases,
        processors=processors
    )


@app.route('/employees')
def view_employees_page():
    employees = UserService.get_all_employees()
    return render_template("employees.jinja",employees=employees)


@app.route('/phones/new', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin')


def view_new_product():
    form = forms.AddPhoneForm(request.form)
    employee = UserService.get_employees()
    battery = PartService.get_batteries()
    case = PartService.get_cases()
    processor = PartService.get_processors()
    form.cases_id_case.choices = [(item['id_case'],item['name']) for item in case]
    form.processors_id_processor.choices = [(item['id_processor'],item['name']) for item in processor]
    form.batteries_id_battery.choices = [(item['id_battery'],item['name']) for item in battery]
    form.user_id_employee.choices = [(item['id_user'],item['name']) for item in employee]
    if request.method == 'POST':
        labour_intensity_raw = request.form['labour_intensity'], 
        labour_intensity = labour_intensity_raw[0]

        name_raw = request.form['name'], 
        name = name_raw[0]

        type_raw = request.form['type'], 
        type = type_raw[0]

        user_id_employee_raw= request.form['user_id_employee'],
        user_id_employee =  user_id_employee_raw[0]

        processors_id_processor_raw = request.form['processors_id_processor'], 
        processors_id_processor = processors_id_processor_raw[0]

        cases_id_case_raw=request.form['cases_id_case'],
        cases_id_case = cases_id_case_raw[0]

        batteries_id_battery_raw = request.form['batteries_id_battery'],
        batteries_id_battery = batteries_id_battery_raw[0]

        hourly_rate_raw = UserService.get_hourly_rate_by_id(user_id_employee)
        hourly_rate = hourly_rate_raw[0]

        battery_price_raw = PartService.get_battery_price_by_id(batteries_id_battery)
        battery_price = battery_price_raw[0]

        case_price_raw = PartService.get_case_price_by_id(cases_id_case)
        case_price = case_price_raw[0]

        processor_price_raw = PartService.get_processor_price_by_id(processors_id_processor)
        processor_price = processor_price_raw[0]

        manufacture_price = (float(hourly_rate) * float(labour_intensity)) + processor_price + case_price + battery_price
        final_price = (manufacture_price) * 110 / 100
        img= request.form['img']
        PhoneService.insert_phone(request.form['labour_intensity'], name, type, user_id_employee, processors_id_processor, cases_id_case,batteries_id_battery,manufacture_price,final_price,img)
        flash('Phone inserted')
        

    return render_template('phones_new.jinja', form=form)



@app.route('/users/new', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin')
def view_new_user():
    form = forms.AddUserForm(request.form)
    userType = UserService.get_user_types()
    form.user_type_id.choices = [(item['id'],item['role']) for item in userType]
    if request.method == 'POST':
        password_raw = request.form['password'], 
        password1 = password_raw[0]
        UserService.insert_user(
            login = request.form['login'], 
            password= str(UserService.hash_password(password1)), 
            user_type_id= request.form['user_type_id'], 
            name= request.form['name'],
            surname= request.form['surname'],
            telephone= request.form['telephone'],
            email= request.form['email'],
            hourly_rate= request.form['hourly_rate']
            )
        flash('User inserted')
    return render_template('customer_new.jinja', form=form)

@app.route('/users/delete', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin')
def delete_user():
    users = UserService.get_all_users()
    form = forms.DeleteUserForm(request.form)
    if request.method == 'POST':
        UserService.delete_by_id(request.form['id_user'])
        flash('User deleted')
    return render_template('user_delete.jinja', form=form)



@app.route('/users/edit', methods=['GET', 'POST'])
@auth.login_required
def view_edit_user():
    form = forms.EditUserForm(request.form)
    if request.method == 'POST': 
        if(request.form['login']):login = request.form['login'] 
        else: login = session['login']
        if(request.form['password']):password = request.form['password']
        else: password = session['password']
        if(request.form['name']):name = request.form['name']
        else: name = session['name']
        if(request.form['surname']):surname = request.form['surname']
        else: surname = session['surname']
        if(request.form['telephone']):telephone = request.form['telephone']
        else: telephone = session['telephone']
        if(request.form['email']):email = request.form['email']
        else: email = session['email']
        id_user=session['id_user']

        UserService.update_user(login, password, name, surname, telephone, email, id_user)
        flash('User edited')
    return render_template('user_edit.jinja', form=form)



@app.route('/signin', methods=['GET', 'POST'])
def view_sign_in():
    form = forms.SignInForm(request.form)
    if request.method == 'POST':
        user = UserService.verify(
            login = request.form['login'],
            password = request.form['password'],
        )
        if user:
            session['authenticated'] = 1
            session['login'] = user['login']
            session['role'] = user['role']
            session['id_user'] = user['id_user']
            session['password'] = user['password']
            session['name'] = user['name']
            session['surname'] = user['surname']
            session['telephone'] = user['telephone']
            session['email'] = user['email']
            return redirect(url_for('index'))
            #masterchief - password
        else:
            flash('Incorrect login or password')
    return render_template("sign_in.jinja", form=form)


@app.route('/signout')
def signout():
    session.pop('authenticated')
    session.pop('login')
    #key error
    session.pop('role')
    return redirect(url_for('index'))

    

@app.route('/edit', methods=['GET', 'POST'])
def view_edit():
    login =  session['login']
    password = session['password']
    name = session['name']
    surname =  session['surname']
    telephone =session['telephone']
    email =session['email']
    return render_template("edit.jinja", login=login, password=password, name=name, surname=surname, telephone=telephone, email=email)

    