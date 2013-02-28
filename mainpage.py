'''
Created on Dec 1, 2012

@author: mark
'''
import webapp2
from envdef import Handler
#from dbfunc import 

HTML_TEMPLATE = "mainpage.html"

class MainPage(Handler):
    def get(self, arg):
        user = self.testCookie('user')
        if not user:
            self.redirect("/login")
            return
        
        self.render( HTML_TEMPLATE, username=user )
        
    def post(self, arg):
        self.redirect("/")
        
app = webapp2.WSGIApplication([('/(.*)', MainPage)], debug=True)
