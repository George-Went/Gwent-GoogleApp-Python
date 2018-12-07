import datetime
import jinja2
import os
import webapp2

from google.appengine.api import users

template_env = jinja2.Environment(loader=jin ja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):

        current_time = datetime.datetime.now()
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)

        template = tempalte_env.get_template('home.html')
        context

        message = '<p>The time is: %s</p>'  % datetime.datetime.now()
        self.response.out.write(message)

application = webapp2.WSGIApplication([('/', MainPage)],
                                        debug=True)