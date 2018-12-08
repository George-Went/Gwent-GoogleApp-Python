from google.appengine.api import users
from google.appengine.ext import ndb
#Sets up model for ndb
class UserPreferances(ndb.Model):

    tz_offset = ndb.FloatProperty(default=0.0) # timezone offset 
    user = ndb.UserProperty(auto_current_user_add=True) # user email



def get_userPreferances(user_id=None):
    if not user_id:
        user = users.get_current_user()
        if not user:
            return None
        user_id = user.user_id()

    key = ndb.Key('UserPreferances', user_id)

    userPreferances = key.get()
    if not userPreferances:
        userPreferances = UserPreferances(id=user_id)
    return userPreferances

