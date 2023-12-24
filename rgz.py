from flask import Blueprint, render_template, request, abort, jsonify
from datetime import datetime

rgz = Blueprint('rgz', __name__)

@rgz.route('/rgz/')
def main():
    return render_template('rgz/index.html')

goods = [
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"},
    {"name": "Холодильник", "art": 123, "count": 3, "price": 3000, "createdAt": "2023-12-12"},
    {"name": "Микроволновка", "art": 456, "count": 3, "price": 4000, "createdAt": "2023-12-17"},
    {"name": "Стиральная машина", "art": 789, "count": 3, "price": 20000, "createdAt": "2023-12-15"}

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
def del_good(course_num):
    if course_num < 0 or course_num >= len(goods):
        return 'Good not found', 404
    del goods[course_num]
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
    good['createdAt'] = datetime.now()
    goods.append(good)
    return {"num": len(goods)-1}