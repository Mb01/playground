'''
Created on Dec 2, 2012

@author: mark
'''
from dbfunc import checkCred
from envdef import Handler, webapp2


def_template = "login.html"

class Login(Handler):
    def get(self):
        self.render(def_template)
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        
        test, username, rating = checkCred(username, password)
        if test:
            self.setCookie('user', username)
        if rating:
            self.setCookie('rating', username+str(rating))
        self.redirect("/")


app = webapp2.WSGIApplication([('/login', Login)], debug=True)