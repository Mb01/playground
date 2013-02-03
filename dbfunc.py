'''
Created on Dec 3, 2012

@author: mark
'''
import logging
import random
from secrets import makeHash, testHash, makeCookieHash
from dbdef import User, Question, db
from cache_util import mems, memg

def getGenreList():
    genreList = ['general','math','geography', 'trivia']
    return genreList

def getQuestionKeys(genre, update=False):
    '''memset all the KEYS under the GENRE return the keys'''
    questions = memg(genre)
    if (not questions) or update:
        questions = Question.all(keys_only=True).filter("genre =", genre)
        questions = [x for x in questions]
        mems(genre, questions)
    return questions
            
def createQuestion(q, a, c1, c2, c3, genre):
    '''db and memset the question with the KEY'''
    quest = Question(question=q, rating=1200.0, votes=0, answer=a, choice1=c1,choice2=c2,choice3=c3, genre=genre)
    quest.put()
    mems( str(quest.key()), quest )
    logging.info("question: " + q + " created.")
    
def getQuestion(genre):
    '''to get a question by genre'''
    if not genre:
        genre = "general"
    questions = getQuestionKeys(genre)
    if not questions:
        logging.error("dbfunc.py line 39: couldn't return a question for: " + genre)
        questions = getQuestionKeys("general")
    ranChoice  = random.choice(questions)
    #not in cache get from db set cache
    q = memg( str(ranChoice) )
    if not q:
        q = db.get(ranChoice)
        mems(str(ranChoice), q)
    q = q.asDict()
    options = [q['answer'], q['choice1'], q['choice2'], q['choice3']]    
    random.shuffle(options)
    q['options'] = options
    q['hashed'] = makeCookieHash(q['answer'])
    return q
  
def voteQuestion(up, key):#up=1 down=0 that's "up?"
    question = Question.get(key)
    if up:
        question.votes += 1
    else:
        question.votes -= 1
    if question.votes < -10:
        db.delete(key)
        getQuestionKeys(update=True)
    else:
        question.put()
   
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



#updateRaing and subfunctions
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

def updateRating(username, userRating, qK, qRating, result):
    user = User.all().filter("username =", username).get()
    question = Question.get(qK)
    user.rating, question.rating = getNewRatings(userRating, qRating, result)
    user.put()
    question.put()
    return str(user.rating)
    
        
        
