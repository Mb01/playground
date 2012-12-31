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
    points = db.IntegerProperty(required=False)
    privilageLevel = db.IntegerProperty(required=False)
    
    def asDict(self):
        d ={
            "username": self.username,
            "password": "secret",
            "email": self.email,
            "created": self.created,
            "points": self.points,
            "privilageLevel": self.privilageLevel
            }
        return d


class Question(db.Model):
    question = db.TextProperty(required=True)
    points = db.IntegerProperty(required=True)
    votes = db.IntegerProperty(required=True)
    
    def asDict(self):
        d = {
             "question" : self.question,
             "points": self.points
             }
        return d
