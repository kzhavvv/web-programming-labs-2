from flask import Blueprint, redirect, url_for,render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    errorss={}
    age = request.args.get('age')
    if age == '':
        errorss['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors, errorss=errorss)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    if request.args.get('cinnamon') == 'on':
        price += 0
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/bilet')
def bilet():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    errorss={}
    age = request.args.get('age')
    if age == '':
        errorss['age'] = 'Заполните поле!'
    city = request.args.get('city')
    if city == '':
        errorss['city'] = 'Заполните поле!'
    date = request.args.get('date')
    if date == '':
        errorss['date'] = 'Заполните поле!'

    return render_template('bilet.html',user=user, age=age, errors=errors, errorss=errorss,city=city,date=date )


@lab3.route('/lab3/kupleno')
def kupleno():
    return render_template('kupleno.html')