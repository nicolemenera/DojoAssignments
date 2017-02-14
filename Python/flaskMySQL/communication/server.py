from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = "llamallamallamamoo"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/emails', methods=['POST', 'GET'])
def handle_request():
  if request.method == 'POST':
    if len(request.form['email']) < 1:
      flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
      flash("Invalid Email Address!")
    else:
      query = "INSERT INTO users (email, create_time, update_time) VALUES (:email, NOW(), NOW())"
      data = {
        'email': request.form['email'], 
      }
      mysql.query_db(query, data)
      flash("Success!")
    return redirect('/emails')
  elif request.method == 'GET':
    query = 'SELECT * FROM users'
    users = mysql.query_db(query)
    return render_template("success.html", users=users)
    
@app.route('/delete', methods=['POST'])
def delete():
  query = "DELETE FROM users WHERE email ='" + request.form['email'] + "'"
  data = {'email': request.form['email']}
  print query
  mysql.query_db(query)
  return redirect('/emails')
    
app.run(debug=True)
  