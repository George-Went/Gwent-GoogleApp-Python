import webapp2

import models

class PrefsPage(webapp2.RequestHandler):
    def post(self):
        userPreferances = models.get_userPreferances()
        try:
            tz_offset = float(self.request.get('tz_offset'))
            userPreferances.tz_offset = tz_offset 
            userPreferances.put()
        except ValueError:
            # User entered a value that was not a float. Igonre for now.
            pass
        self.redirect('/')

application = webapp2.WSGIApplication([('/prefs',PrefsPage)],
                                         debug=True)

#This handels the HTTP POST reuest to the app to the url /prefs
# because it is a POST the def is "post" not "get" 