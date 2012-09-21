import os
import jinja2
import cgi,re
import webapp2


jinja_environment = jinja2.Environment(autoescape=True,
                                       loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))



class MainPage(webapp2.RequestHandler):
                                  
  def get(self):
    self.response.headers['Content-Type']='text/html'
    
    
      
      
class MainPage2(webapp2.RequestHandler):
  def get(self):
    template_values={}
    template = jinja_environment.get_template('flame.html')
    self.response.out.write(template.render(template_values))
                               
app = webapp2.WSGIApplication(
[('/',MainPage2)],debug = True
)

