from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html', name="Nikki")

  
@app.route('/ninjas')
def success():
  return render_template('ninjas.html')
  
  
@app.route('/dojos')
def dojo():
  return render_template('dojos.html')
  
app.run(debug=True)