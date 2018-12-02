#This file is used for specifying where app engine should look for third party libraries
from google.appengine.ext import vendor

#add any libraries installed in the "lib" folder
vendor.add('lib')
