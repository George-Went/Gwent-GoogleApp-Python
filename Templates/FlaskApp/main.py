#!/usr/bin/env python
from flask import Flask, render_template, request

#from google.appengine.ext import ndb

#class MitigatingCircumstance(ndb.Model):
#    name = ndb.StringProperty()
#    phone = ndb.StringProperty() 
#    issue = ndb.StringProperty()
#    comment = ndb.StringProperty()

#class MitigatingCircumstance(Form)

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/hteeml")
def hteeml():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/salvador")
def salvador():
    return render_template("salvador.html")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted_form', methods=['POST'])
def submitted_form():
    name = request.form['name']
    phone = request.form['phone']
    issue = request.form['issue']
    comment = request.form['comment']

    return render_template(
    'submitted_form.html',
    name=name,
    phone=phone,
    issue=issue,
    comment=comment)

if __name__ == "__main__":
    app.run(debug=True)