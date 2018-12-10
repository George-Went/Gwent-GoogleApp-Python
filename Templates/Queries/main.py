from google.appengine.ext import ndb
import datetime



class Player(ndb.Model): 
    name = ndb.StringProperty()
    level = ndb.IntergetProperty()
    score = ndb.IntergerProperty()
    charclass = ndb.StringProperty()
    create_date = ndb.DateTimeProperty(auto_now_add=True)

player1 = Player(
    name='wizard123',
    level=1,
    score=32,
    charclass='mage'
)
player1.put()

player2 = Player(
    name='druidman',
    level=12,
    score=64,
    charclass='druid'
)
player2.put()

player3 = Player(
    name='legend27',
    level=50,
    score=345,
    charclass='warrior'
)
player3.put()

