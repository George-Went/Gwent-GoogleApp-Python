import webapp2
import jinja2

from views import *

application = webapp2.WSGIApplication(
[
    ('/', MainPage),
    ('/george', George),
    ('/Form', Form),
    ('/Submit', Submit),
    ('/FormExample', FormExample),
    ('/SubmitExample', SubmitExample),
    ('/CreateStudent', CreateStudent),
],
                                        debug=True)