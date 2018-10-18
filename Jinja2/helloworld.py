import jinja2
import os 
import webapp2


template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
#This gloabal variable allows the template to be read across the 
#application, it tells the filesystemloader that the template are in the 
#current directory

class MainPage(webapp2.RequestHandler): 
    def get(self): 

        string = 'Hello World' 

        template = template_env.get_template('helloworld.html')
        context = {
            'string': string, 
        } 
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage)],
                                        debug=True)
#The Web Server Gateway Interface is part of the webapp2 framework 
#It is similar to the Django framework1`