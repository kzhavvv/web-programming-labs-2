from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask import session 
import psycopg2


lab5 = Blueprint('lab5', __name__)

def dbConnect():
    #подключение к бд
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "karina_knowledge_base",
        password = "123")  
    return conn;

def dbClose(cursor, connection):
    #закрываем курсор и соединение 
    #курсор - память, которая хранит  набор select 
    #select возвращает данные
    cursor.close()
    connection.close()


@lab5.route('/lab5')
def main():
    conn = dbConnect()
    cur = conn.cursor()
    #запрос, который psycopg2 должен выполнить 
    cur.execute("SELECT * FROM users;")
    #fetchall - получить все строки, которые получились в результате
    #выполнения SQL-запроса в execute
    result = cur.fetchall()

    print(result)
    #закрытие соединения с БД
    dbClose(cur,conn)

    return "go to console"


@lab5.route('/lab5/')
def lab():
    user_name = session.get('user_name')
    return render_template('lab5.html', user_name=user_name)


@lab5.route('/lab5/reg', methods=["GET", "POST"])
def reg():
    errors = []
    #если это метод GET, то вернуть шаблон и завершить выполнение
    if request.method == "GET":
        return render_template('reg.html', errors=errors)
    #если мы здесь, то это метод POST    
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    #Проверка username u password на пустоту
    #если из них кто-то пустой, то добавим ошибку и рендерим шаблон
    if not (user_name or password):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('reg.html', errors=errors)
    #получаем пароль от пользователя и хешируем его
    hashPassword = generate_password_hash(password)
    #если мы тут, то значит username u password заполнены 
    #подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()
    #проверяем наличие клиента в бд
    #у нас не может быть два пользователя с одинаковыми логинами
    cur.execute("SELECT username FROM users WHERE username = %s;", (user_name,))
    #fetchone получает одну строку
    #только один пользователь может быть с таким именем в бд
    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        conn.close()
        cur.close()
        return render_template('reg.html', errors=errors)
    #если мы попали сюда, то значит в cur.fetchone нет ни одной строки
    #пользователя с таким логином не существует
    #сохраняем пароль в виде хэша Бд   
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (user_name, hashPassword))
    #делаем commit - т.е. фиксируем изменени
    conn.commit()
    conn.close()
    cur.close()
    return redirect("/lab5/loginn")


@lab5.route('/lab5/anon')
def anon():
    VisibleUser = "Anon"
    return render_template('anon.html', username=VisibleUser)


@lab5.route("/lab5/newtitle", methods = ["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get('id')
    user_name = session.get('user_name')
    if userID is not None:
        if request.method =="GET":
            return render_template("newtitle.html", user_name=user_name)
        
        if request.method == "POST":
            article_text = request.form.get("article_text")
            title = request.form.get("article_title")

            if len(article_text)==0:
                errors.append("Заполните текст")
                return render_template("new_article", errors = errors, user_name=user_name)
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, article_text))
            
            
            new_articl_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_articl_id}")

    return redirect("/lab5/login5")


@lab5.route('/lab5/loginn', methods=["GET", "POST"])
def loginn():
    errors = []

    if request.method == "GET":
        return render_template("loginn.html", errors=errors)
    
    user_name = request.form.get("username")
    password = request.form.get("password")

    if not (user_name or password):
        errors.append("Пожалуйста заполните все поля")
        return render_template("loginn.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (user_name,))

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("loginn.html", errors=errors)
    
    userID, hashPassword = result
    #с помощью check_password_hash сравниваем пароль и хэш из бд
    if check_password_hash(hashPassword, password):
        #пароль правильный 

        #сохраняем id u username в сессию 
        session['id'] = userID
        session['user_name'] = user_name
        dbClose(cur, conn)
        return redirect("/lab5/")
    
    else:
        errors.append("Неправильный логин или пароль")
        return render_template("loginn.html", errors=errors)


@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):

    userID = session.get('id')
    #проверка авторизирован ли пользователь
    if userID is not None:

        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s AND user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        #разбиваем строку на массив по "Enter",чтобы с помощью цикла for разбить статью на параграфы 
        text = articleBody[1].splitlines()

    return render_template("articleN.html", article_text=text, article_title=articleBody[0], user_name=session.get("user_name"))



@lab5.route('/lab5/articles')
def list_articles():
    #проверяем авторизирован ли пользователь
    userID = session.get('id')
    user_name = session.get("user_name")
    #если пользователь авторизирован
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        
        cur.execute("SELECT id, title FROM articles WHERE user_id = %s;", (userID,))
    #получаем id от вновь созданной записи, получаем статьи след.образом /lab5/articles/id_articles
        articles_data = cur.fetchall()
        
        articles = [{'id': row[0], 'title': row[1]} for row in articles_data]

        dbClose(cur, conn)

        return render_template('articles.html', articles=articles, user_name=user_name)
    #пользователь не авторизирован
    return redirect("/lab5/loginn")

@lab5.route('/lab5/logout', methods=["GET"])
def logout():
    session.clear()
    return redirect("/lab5/loginn")