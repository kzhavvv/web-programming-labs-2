from flask import Blueprint, render_template, request, abort, redirect, jsonify
from db import db

from db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

rgz = Blueprint('rgz', __name__)

@rgz.route('/rgz/')
def main():
    return render_template('rgz/registr.html')

goods = [
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000,},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000,},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000,},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000,},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000,},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000,},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000,},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000}

]

@rgz.route('/rgz/api/goods/', methods=['GET'])
def get_goods():
    return jsonify(goods)


@rgz.route('/rgz/api/goods/<int:good_num>', methods=['GET'])
def get_good(good_num):
    if good_num < 0 or good_num > len(goods):
        return "Курс не найден", 404
    return goods[good_num]


@rgz.route('/rgz/api/goods/<int:good_num>', methods=['DELETE'])
def del_good(good_num):
    if good_num < 0 or good_num >= len(goods):
        return 'Good not found', 404
    del goods[good_num]
    return '', 204


@rgz.route('/rgz/api/goods/<int:good_num>', methods=['PUT'])
def put_good(good_num):
    if good_num < 0 or good_num >= len(goods):
        return 'Good not found', 404
    good = request.get_json()
    goods[good_num] = good
    return goods[good_num]


@rgz.route('/rgz/api/goods/', methods=['POST'])
def add_good():
    good = request.get_json()
    goods.append(good)
    return {"num": len(goods)-1}


@rgz.route('/rgz/registr', methods=["GET", "POST"])
def registrPage():
    errors = []

    if request.method == "GET":
        return render_template('registr.html', errors=errors)
     
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    
    hashPassword = generate_password_hash(password_form, method='pbkdf2')

    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        errors.append("Пользователь уже существует")
        return render_template('registr.html', errors=errors)
    
    if username_form is None or password_form is None or username_form.strip() == '' or password_form.strip() == '':
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template('registr.html', errors=errors)
    if len(password_form) < 5:
            errors.append("Пароль должен содержать не менее 5 символов")
            print(errors)
            return render_template('registr.html', errors=errors)

    

    newUser = users(username=username_form, password=hashPassword)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/rgz/login')


@rgz.route('/rgz/login', methods = ['GET', 'POST'])
def login():
    errors = []
    if request.method == 'GET':
        return render_template('login.html')

    username_form = request.form.get('username')
    password_form = request.form.get('password')

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember = False)
            return redirect('/rgz/glav')
        else: 
            errors.append("Неправильный пароль")
            return render_template('login.html', errors=errors)
        
    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login.html", errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login.html', errors=errors)
    
    else: 
        errors.append('Пользователя не существует')
        return render_template('login.html', errors=errors)

    

@rgz.route('/rgz/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/rgz/glav')
