from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)


@lab1.route("/")


@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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
            <li><a href="/lab3">Третья лабораторная</a></li>
            <li><a href="/lab4">Четвертая лабораторная</a></li>
            <li><a href="/lab5/">Пятая лабораторная</a></li>
        <ol>
        <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1")
def lab():
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
        <li><a href="lab1/student">lab1/oao/-student</a></li>
        <li><a href="/lab1/python">pythnon</a></li>
        <li><a href="/lab1/kachely">lab1/kak/песенка</a></li>
        <ol>

        <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

"""


@lab1.route("/lab1/oak")
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


@lab1.route("/lab1/student")
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


@lab1.route("/lab1/python")
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


@lab1.route("/lab1/kachely")
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
        <br>В старом парке тает снег,
        <br>И весёлые качели
        <br>Начинают свой разбег.
        <br>Позабыто всё на свете,
        <br>Сердце замерло в груди,
        <br>Только небо, только ветер,
        <br>Только радость впереди.
        <br>Только небо, только ветер,
        <br>Только радость впереди.
        </b>
        </p>
        <p>
        <b>
        <br>Взмывая выше ели,
        <br>Не ведая преград,
        <br>Крылатые качели
        <br>Летят, летят, летят.
        <br>Крылатые качели
        <br>Летят, летят, летят.
        </b>
        </p>
        <p>
        <b>
        <br>Детство кончится когда-то,
        <br>Ведь оно не навсегда,
        <br>Станут взрослыми ребята,
        <br>Разлетятся кто куда.
        <br>А пока мы только дети,
        <br>Нам расти ещё расти,
        <br>Только небо, только ветер,
        <br>Только радость впереди.
        <br>Только небо, только ветер,
        <br>Только радость впереди.
        </b>
        </p>
        <img class="py" src="''' + url_for('static', filename='kak.jpg') +  '''">
    </body>
    <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
    </footer>
</html>
'''