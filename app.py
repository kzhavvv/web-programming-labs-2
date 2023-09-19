from flask import Flask
app = Flask(__name__)
@app.route("/")
def start():
    return """
<!doctype html>
<html lang="ru">
    <head>
    </head>
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
        &copy; Жвавий Карина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""
