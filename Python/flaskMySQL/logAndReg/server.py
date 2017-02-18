from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_registration')
app.secret_key = "llamallamallamamoo"

@app.route('/')
def index():
  return render_template("index.html")
  
@app.route('/create_user', methods=['POST'])
def create_user():
  print 'HELLOOOOO'
  first_name = request.form['name_first']
  last_name = request.form['name_last']
  email = request.form['email_address']
  password = request.form['password']
  password_conf = request.form['confirm_password']
  pw_hash = bcrypt.generate_password_hash(password_conf)
  #pdb.set_trace()

  if first_name == '':
    flash("First name is required")
    return redirect ('/')
  if last_name == '':
    flash("Last name is required")
    return redirect ('/')
  if email == '':
    flash("Email address is required")
    return redirect ('/')
  if not EMAIL_REGEX.match(email):
    flash("Invalid Email Address")
    return redirect ('/')
  if password == '':
    flash("Password is required and must be at least 8 characters long")
    return redirect ('/')
  if len(password) >1 and len(password) <8:
    flash("Password must be at least 8 characters long")
    return redirect ('/')
  if password_conf != password:
    flash("Confirmation password and password must match")
    return redirect ('/')
  else:
    print 'HELLO'
    query = "INSERT INTO users (first_name, last_name, email, pw_hash, create_at, update_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
    data = {
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'pw_hash': pw_hash
    }
    mysql.query_db(query, data)
    flash("Success! You may now log in below!")
  return render_template('success.html', is_new=True)
  
  
@app.route('/log_in', methods=['POST'])
def log_in():
  email = request.form['email_address']
  password = request.form['password']
  user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
  query_data = {'email':email}
  user = mysql.query_db (user_query, query_data)
  if bcrypt.check_password_hash(user[0]['pw_hash'], password):
    if "user" not in session:
      session ["user"] = " "
    return render_template('success.html', is_new=False)
  else:
    error = 'Password incorrect!'
  return render_template('index.html')

app.run(debug=True)