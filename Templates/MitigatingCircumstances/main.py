import webapp2
import jinja2



from views import *

application = webapp2.WSGIApplication(
[
  #  ('/',MainPage),
    ('/students',StudentIndex),
    # ('/students/<id:\d+'),
    # ('/view'),
    # ('/students'),
    # ('/students'),
    # ('/students'),
    # ('/students'),
    #webapp2.Route('/view-submissions',handler = MainPage, name = 'home'),
],
                                        debug=True)