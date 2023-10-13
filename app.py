from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)
@app.route("/menu")
def menu():
    return """
<!doctype html>
<html lang="ru">
    <head>
    «НГТУ, ФБ, Лабораторные работы»
    </head>
    <body>
        <header>
            <title>НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных</title>
        </header>
        <ol>
            <li><a href="/lab1">Первая лабораторная</a></li>
            <li><a href="/lab2">Вторая лабораторная</a></li>
        <ol>
        <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html lang="ru">
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
    <head>
    </head>
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <a href="/menu">меню</a>
        <h2>Реализованные роуты</h2>
        <ol>
        <li><a href="lab1/oak">lab1/oak/-дуб</a></li>
        <li><a href="lab1/oao">lab1/oao/-student</a></li>
        <li><a href="/lab1/python">pythnon</a></li>
        <li><a href="/lab1/kachely/">lab1/kak/песенка</a></li>
        <ol>

        <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

"""
@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>
    <body>
        <h1 class="dub">Дуб</h1>
        <img class="oak" src="''' + url_for('static', filename='oak.jpg') +  '''">
    </body>
    <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
    </footer>
</html>
'''
@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <body>
        <h1 class="dub">Жвавий Карина Алексеевна</h1>
        <img class="oao" src="''' + url_for('static', filename='oao.jpg') +  '''">
    </body>
    <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
    </footer>
</html>
'''
@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <body>
        <p>
        <b>
        Первая версия Python была разработана в 1991 году программистом из Нидерландов Гвидо ван Россумом. 
        В настоящее время выходят новые версии языка, которые расширяют его возможности, а сам он занимает верхние 
        строчки рейтингов языков программирования. Python применяется во многих сферах: веб-разработка, анализ данных 
        и машинное обучение и др.</b>
        </p>
        <p>
        <b>
        Главное достоинство Python — простота синтаксиса и команд, а также большое количество библиотек, которые 
        содержат уже написанный программный код для решения широкого спектра задач. Python даже применяют в своих 
        исследованиях и разработках специалисты, чьи профессии напрямую не связаны с программированием. Один из самых 
        частых примеров — применение Python для анализа большого количества данных и нахождения корреляции между ними.</b>
        </p>
        <p>
        <b>
        Все языки программирования можно условно разделить на две большие группы: компилируемые и интерпретируемые.
        Программы, написанные на компилируемых языках программирования, преобразуются (компилируются) в машинный код и 
        становятся исполняемыми (например, в операционной системе Windows это чаще всего будет файл с расширением .exe). 
        Программы, написанные на интерпретируемых языках (в их числе и Python),
        не компилируются, и для их запуска требуется специальная программа — интерпретатор.<b>
        </p>
        <img class="py" src="''' + url_for('static', filename='py.jpg') +  '''">
    </body>
    <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
    </footer>
</html>
'''
@app.route("/lab1/kachely")
def kachely():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <body>
        <p>
        <b>
        В юном месяце апреле
        В старом парке тает снег,
        И весёлые качели
        Начинают свой разбег.
        Позабыто всё на свете,
        Сердце замерло в груди,
        Только небо, только ветер,
        Только радость впереди.
        Только небо, только ветер,
        Только радость впереди.
        </b>
        </p>
        <p>
        <b>
        Взмывая выше ели,
        Не ведая преград,
        Крылатые качели
        Летят, летят, летят.
        Крылатые качели
        Летят, летят, летят.
        </b>
        </p>
        <p>
        <b>
        Детство кончится когда-то,
        Ведь оно не навсегда,
        Станут взрослыми ребята,
        Разлетятся кто куда.
        А пока мы только дети,
        Нам расти ещё расти,
        Только небо, только ветер,
        Только радость впереди.
        Только небо, только ветер,
        Только радость впереди.
        </b>
        </p>
        <img class="py" src="''' + url_for('static', filename='kak.jpg') +  '''">
    </body>
    <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
    </footer>
</html>
'''
@app.route('/lab2/example')
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
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')
@app.route('/lab2/kreedik')
def kredeek():
    return render_template('kreed.html')
