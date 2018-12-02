#!/usr/bin/env python
from flask import Flask, render_template, request

from google.appengine.ext import ndb

class MitigatingCircumstance(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty() 
    issue = ndb.StringProperty()
    comment = ndb.StringProperty()

#class MitigatingCircumstance(Form)

#name of the application that uses the flask framework
app = Flask(__name__)

@app.route("/")
def home():
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

    submission = name + 'MitigatingCirtumstance' 

    submission = MitigatingCircumstance(name = request.form['name'],
                                    phone = request.form['phone'],
                                    issue = request.form['issue'],
                                    comment = request.form['comment'])
    
    submission.put()


    return render_template(
    'submitted_form.html',
    name=name,
    phone=phone,
    issue=issue,
    comment=comment)

@app.route('/view_submissions')
def form():
    
    def get_submissions()
    key = ndb.

    

    return render_template('form.html')





if __name__ == "__main__":
    app.run(debug=True)