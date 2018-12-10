# App Egine 






# NDB CRUD



The first step is to import the ndb packages from the google app development files

```python
from google.appengine.ext import ndb
```

## Creating a model

A model consists of its variables and 3 types of referance:
* Kind - what the objects entity is (same as a object class)
* ID - the idetifier fo each type of object
* Key - a unique identifier for each induvidual object

###Creating the model
```python
    class CarModel(ndb.Model): #google noSQL model creation  
    company = ndb.StringProperty()
    model = ndb.StringProperty()
    doors = ndb.IntergerProperty()
    automatic = ndb.BooleanProperty()
```

