'''
Created on Dec 1, 2012

@author: mark
'''
import webapp2
from envdef import Handler


HTML_TEMPLATE = "mainpage.html"

class MainPage(Handler):
    def get(self, arg):
        user = self.testCookie('user')
        rating = str(self.testCookie('rating'))[len(user):len(user)+7]
        if not user:
            self.redirect("/login")
             
        self.render(HTML_TEMPLATE, username=user, rating=rating)#arg=arg etc...
        
    def post(self, arg):
        self.redirect("/")
        
app = webapp2.WSGIApplication([('/(.*)', MainPage)], debug=True)
