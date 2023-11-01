from flask import Blueprint, redirect, url_for,render_template, request
lab4 = Blueprint('lab4',__name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form.get('username')
    password = request.form.get('password')
    error = None 
    if not username and not password:
        error = 'Нет логина и пароля'
    elif not username:
        error = 'Нет логина'
    elif not password:
        error = 'Нет пароля'
    elif username == 'kzhavvv' and password == '2023':
        return render_template("entrance.html", username=username)
    else:
        error = 'Неверный логин или пароль!'

    return render_template("login.html", error=error, username=username, password=password)


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template("fridge.html")
    
    temperature = request.form.get('temperature')
    if  not temperature:
        result = 'ошибка: не задана температура!'
    elif int(temperature) < -12:
        result = 'не удалось установить температуру — слишком низкое значение'
    elif int(temperature) > -1:
        result = 'не удалось установить температуру — слишком высокое значение'
    elif int(temperature) > -12 and int(temperature) < -9:
        result = f"Установлена температура: {temperature}°C ***"
    elif int(temperature) >= -8 and int(temperature) <= -5:
        result = f"Установлена температура: {temperature}°C **"
    elif int(temperature) >= -4 and int(temperature) <= -1:
        result = f"Установлена температура: {temperature}°C *"

    return render_template("fridge.html", result=result)


@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template("zerno.html")
    grain = request.form.get('grain')
    weight = float(request.form.get('weight'))
    price = 0
    skidka = None

    if grain == 'Ячмень':
        price = 12000
    elif grain == 'Овёс':
        price = 8500
    elif grain == 'Пшеница':
        price = 8700
    elif grain == 'Рожь':
        price = 14000
    else:
        price = 0
    
    summ = price * weight
    if weight >= 50 and weight <= 500:
        summ = (price * weight) * 0.9
        skidka_itog = (price * weight) * 0.1
        skidka = f'Скидка 10% за объём более 50 тон: = {skidka_itog}'
    elif weight < 50:   
        skidka = 'Скидка 10% за объём не присвоена'
    else:
        skidka = None

 
    if weight > 500:
        errors = 'Такого объема нет в наличии'
        return render_template("zerno.html", errors=errors)
    elif weight < 0:
        errors = 'Не верно указан объём закупки'
        return render_template("zerno.html", errors=errors)
    
    return render_template("zerno.html", grain=grain, weight=weight, summ=summ, skidka=skidka)