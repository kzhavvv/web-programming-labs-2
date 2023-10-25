from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route('/lab2/example')
def example():
    name= 'Жвавий Карина'
    group = 'ФБИ-14'
    curs ='3 курс'
    laba = 'Лабораторная работа 2'
    5+2== ''
    11*28==''
    8452/793==''
    45**(8)==''
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80}, 
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321}
        ]
    books =[
        {'bk': 'Оно', 'autor': 'Стивен Кинг', 'genre': 'роман','pages': 1138 },
        {'bk': 'Три товарища', 'autor': 'Эрих Мария Ремарк', 'genre': 'роман','pages': 480 },
        {'bk': 'Портрет Дориана Грея', 'autor': 'Оскар Уайльд', 'genre': 'роман','pages': 400 },
        {'bk': 'Не ной', 'autor': 'Джен Синсеро', 'genre': 'Саморазвитие','pages': 292 },
        {'bk': '451° по Фаренгейту', 'autor': 'Рей Бредбери', 'genre': 'антиутопия','pages': 256 },
        {'bk': 'Гарри Поттер', 'autor': 'Джоан Роулинг', 'genre': 'фэнтези','pages': 248 },
        {'bk': 'После', 'autor': 'Анна Тод', 'genre': 'Современная проза','pages': 448 },
        {'bk': 'Маленький принц', 'autor': 'Антуан де Сент-Экзюпери', 'genre': 'повесть','pages': 110 },
        {'bk': 'Великий Гэтсби', 'autor': 'Фрэнсис Скотт Фицджеральд', 'genre': 'роман','pages':256  },
        {'bk': 'Дневник Анны Франк', 'autor': 'Анна Франк', 'genre': 'мемуар','pages': 280 }
    ]
    return render_template('example.html',name=name,group=group,curs=curs,laba=laba,fruits=fruits,books=books)
@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/kreedik')
def kredeek():
    return render_template('kreed.html')