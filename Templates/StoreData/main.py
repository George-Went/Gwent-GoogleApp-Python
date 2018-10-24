import datetime
import jinja2
import os 
import webapp2

from google.appengine.ext import ndb

class Drink(ndb.Model):
    name = ndb.StringProperty()


class MainPage(webapp2.RequestHandler):

    def get(self):  
        milk = Drink(name='milk')
        milk.put()



application = webapp2.WSGIApplication([('/addmilk', MainPage)],
                                        debug=True)

