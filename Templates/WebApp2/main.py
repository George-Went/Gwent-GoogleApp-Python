import webapp2
import os 
import cgi
import jinja2

from google.appengine.ext import ndb

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
    def get(self):
        name = "Micha"
        message = '<p>Hello %s</p>'  % name #the %s is the string input for the html
        self.response.out.write(message) #when a request is recived this line is the 
                                         #return equivelent 


class George(webapp2.RequestHandler):
    def get(self):
        name = "george"
        message = '<p>Hello %s</p>'  % name
        self.response.out.write(message)

class Me(webapp2.RequestHandler):
    def get(self): 
        template = template_env.get_template('templates/form.html')
        context = {
            'name': "George",
            'lecturer': "Tim",
            'issue': "cant do REST",
            'comment': "halp",
        } 
        self.response.out.write(template.render(context))

class MitigatingCircumstance(ndb.Model): #google noSQL model creation
    student_name = ndb.StringProperty()

class Form(webapp2.RequestHandler):
    def get(self): 
        template = template_env.get_template('templates/form.html')

        context = {
            'name': "George",
            'lecturer': "lecturer",
            'issue': "dsfsdfsd",
            'comment': "commsdfdsfdsfdsent",
        } 
        self.response.out.write(template.render(context))



class Submit(webapp2.RequestHandler):
    def post(self):#HTTP post data from form page 

        message = self.request.get('name')

        MitigatingCircumstance.student_name = message
        MitigatingCircumstance.put()

        self.response.out.write(message)  #writes the ( gets the ( /form 'name ))

    def get(self): #HTTP GET data from form page 
        template = template_env.get_template('templates/submit_form.html')
        self.response.out.write(template.render())

        name = self.request.get('name')




class FormExample(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/SubmitExample" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")







class SubmitExample(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')




application = webapp2.WSGIApplication(
[
    ('/', MainPage),
    ('/george', George),
    ('/Form', Form),
    ('/Submit', Submit),
    ('/FormExample', FormExample),
    ('/SubmitExample', SubmitExample),
],
                                        debug=True)