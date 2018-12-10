import webapp2
import jinja2



from views import *

application = webapp2.WSGIApplication(
[
  #  ('/',MainPage),
    ('/students',StudentIndex),
    ('/students/(\d+)',StudentShow),
    ('/students/create', StudentCreate),
    ('/students/(\d+)/edit', StudentEdit),
    # ('/students'),
    # ('/students'),
    # ('/students'),
    #webapp2.Route('/view-submissions',handler = MainPage, name = 'home'),
],
                                        debug=True)