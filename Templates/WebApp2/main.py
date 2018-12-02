import webapp2
import os 


class MainPage(webapp2.RequestHandler):
    def get(self):
        name = "Micha"
        message = '<p>Hello %s</p>'  % name
        self.response.out.write(message)


class George(webapp2.RequestHandler):
    def get(self):
        name = "george"
        message = '<p>Hello %s</p>'  % name
        self.response.out.write(message)

class India(webapp2.RequestHandler):
    def get(self):
        message = '<p>Inja went is looser haha</p>'  
        self.response.out.write(message)









application = webapp2.WSGIApplication(
[
    ('/', MainPage),
    ('/george', George),
    ('/india', India),
],
                                        debug=True)