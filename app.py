import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="5156278353Yi",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST',"GET"])
def login():
    if request.method =="POST":
        username = request.form.get('username')
        password = request.form.get('password')
    if password=="" or username=="":
        return render_template('notexist.html')

    try:
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        return render_template('account.html', full_name=records[0][1],password=password,username=username)
    except:
        return render_template('error.html')
