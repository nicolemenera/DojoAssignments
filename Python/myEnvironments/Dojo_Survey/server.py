from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
@app.route('/')

def survey():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!") # just pass a string to the flash function
    else:
        flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
    return redirect('/') 

   return render_template("result.html")
app.run(debug=True) # run our server
