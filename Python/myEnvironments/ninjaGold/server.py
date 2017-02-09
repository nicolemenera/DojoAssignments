from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'bananarama'

@app.route('/')
def index( ):
  if "gold" not in session:
    session ["gold"] = 0
  if "result" not in session:
    session ["result"] = " "
  return render_template('index.html')
  
@app.route('/process_money', methods=["POST"])
def process_money():
  if request.form["building"] == "farm":
     addgold = random.randrange(10,20)
     session['gold'] += addgold
     session["result"] += "Earned " + str(addgold) + " gold from the farm! " + "("+str(datetime.now())+")" + "\n"
  if request.form["building"] == "cave":
     addgold = random.randrange(5,10)
     session['gold'] += addgold
     session["result"] += "Earned " + str(addgold) + " gold from the cave! " + "("+str(datetime.now())+")" + "\n"
  if request.form["building"] == "house":
     addgold = random.randrange(2,5)
     session['gold'] += addgold
     session["result"] += "Earned " + str(addgold) + " gold from the house! " + "("+str(datetime.now())+")" + "\n"
  if request.form["building"] == "casino":
     addgold = random.randrange(-50,50)
     session['gold'] += addgold
     session["result"] += "Earned " + str(addgold) + " gold from the casino! " + "("+str(datetime.now())+")" + "\n"
  if session['gold'] > 50:
     session["no"] = "Yay! Make it Rain!"
  if session['gold'] < 50:
     session["no"] = "You broke, bitch! Go home!"
  return redirect('/')

app.run(debug=True)
