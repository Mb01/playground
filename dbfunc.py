'''
Created on Dec 3, 2012

@author: mark
'''
import logging
from secrets import makeHash, testHash
from dbdef import User, Question 
from cache_util import mems, memg

def getQuestions(update=False):
    questions = memg("_questions123")
    if (not questions) or update:
        if update:
            logging.info("update: questions hits db")
        else:
            logging.info("questions hits db non-update")
        questions = []
        query = Question.all()
        for quest in query:
            questions.append(quest.asDict())
        mems("_questions123", questions)
    else:
        #logging.info("questions hits cache")
        pass
    return questions
            
def createQuestion(q, a, c1, c2, c3):
    quest = Question(question=q, rating=0.0, votes=0, answer=a, choice1=c1,choice2=c2,choice3=c3)
    quest.put()
    logging.info("question: " + q + " created.")
    getQuestions(update=True)


###user functions
def createUser(username, password, email=None):
    password = makeHash(password)
    exists = User.all().filter("username =", username).get()
    if exists:
        return "User " + username + " taken."
    if email:
        user = User(username=username, password=password, email=email)
    else:
        user = User(username=username, password=password)
    user.put()
    logging.info("User: " + username + " created!")

def checkCred(username, password):
    user = User.all().filter("username =", username).get()
    if user:
        passMatch = testHash(user.password, password)
        if passMatch:
            return True, user.username, user.rating
    return False, None, None
