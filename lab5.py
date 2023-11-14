from flask import Blueprint, render_template, request, session, redirect, url_for
import psycopg2


lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "karina_knowledge_base",
        password = "123")  
    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()
@lab5.route('/lab5')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur,conn)

    return "go to console"


@lab5.route('/lab5/')
def lab():
    user_name = session.get('user_name')
    return render_template('lab5.html', user_name=user_name)


@lab5.route('/lab5/reg', methods=["GET", "POST"])
def reg():
    errors = []

    if request.method == "GET":
        return render_template('reg.html', errors=errors)
     
    user_name = request.form.get("user_name")
    password = request.form.get("password")


    if not (user_name or password):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('reg.html', errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{user_name}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
        dbClose(cur, conn)
        return render_template('reg.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{user_name}', '{password}');")
    
    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/loginn")


@lab5.route('/lab5/anon')
def anon():
    VisibleUser = "Anon"
    return render_template('anon.html', username=VisibleUser)


@lab5.route('/lab5/loginn')
def loginn():
    return render_template('loginn.html')


@lab5.route('/lab5/sozdanie')
def sozdanie():
    return render_template('sozdanie.html')


@lab5.route('/lab5/prosmotr')
def prosmotr():
    return render_template('prosmotr.html')