'''
Created on Dec 1, 2012

@author: mark
'''

from google.appengine.ext import db #@UnresolvedImport don't worry be happy


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)
    rating = db.FloatProperty(required=True)
    privilageLevel = db.IntegerProperty(required=False)
    
    def asDict(self):
        d ={
            "username": self.username,
            "password": "secret",
            "email": self.email,
            "created": self.created,
            "rating": self.rating,
            "privilageLevel": self.privilageLevel
            }
        return d

