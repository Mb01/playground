'''
Created on Dec 3, 2012

@author: mark
'''
import logging
import random
from secrets import makeHash, testHash, makeCookieHash
from dbdef import User, db
from cache_util import mems, memg
   
###user functions
def createUser(username, password, email=None):
    password = makeHash(password)
    exists = User.all().filter("username =", username).get()
    if exists:
        return "User " + username + " taken."
    if email:
        user = User(username=username, password=password, email=email, rating=1200.0)
    else:
        user = User(username=username, password=password, rating=1200.0)
    user.put()
    logging.info("User: " + username + " created!")

def checkCred(username, password):
    user = User.all().filter("username =", username).get()
    if user:
        passMatch = testHash(user.password, password)
        if passMatch:
            return True, user.username, user.rating
    return False, None, None



#an elo rating system
def getExpectation(rating_1, rating_2):
    '''generates the expected for rating_1 for modifyRating function'''
    return (1.0 / (1.0 + pow(10, ((rating_2 - rating_1) / 400))))
    
def modifyRating(rating, expected, actual, kfactor=20):#actual -> loss=0 win=1
    '''wrapped by getNewRatings'''
    return (rating + kfactor * (actual - expected))
    
def getNewRatings(rating_1, rating_2, result): #result for player1
    '''return new elo ratings for player1 and player2'''
    player1 = modifyRating(rating_1, getExpectation(rating_1, rating_2), result)
    player2 = modifyRating(rating_2, getExpectation(rating_2, rating_1), 1 - result)
    return player1, player2

#how to use

#def updateRating(username, userRating, questionKey, qRating, result):
#    user = User.all().filter("username =", username).get()
#    question = Question.get(questionKey)
#    user.rating, question.rating = getNewRatings(userRating, qRating, result)
#    user.put()
#    question.put()
#    return str(user.rating)
    
        
        
