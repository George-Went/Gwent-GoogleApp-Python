import datetime
import jinja2
import os 
import webapp2
import model

from google.appengine.api import users
from google.appengine.api import userid

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
#This gloabal variable allows the template to be read across the 
#application, it tells the filesystemloader that the template are in the 
#current directory

class MainPage(webapp2.RequestHandler): 
    def get(self):   
        george = Account()
        george.Username=login_url
        george.userid=123
        george.name='george'
        george.DOB='17/03/1996'
        george.age='22'
        george.height='5.9'

    

        george = george_key.get()

        template = template_env.get_template('home.html')
        context = {
            'user': user,
            'login_url': login_url,
            'logout_url': logout_url,
            'name': george.name,
            'DOB': george.DOB,
            'age': george.age,
            'height': george.height,
        } 
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage)],
                                        debug=True)
#The Web Server Gateway Interface is part of the webapp2 framework 
#It is similar to the Django framework1`