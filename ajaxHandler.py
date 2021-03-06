'''
Created on Dec 29, 2012

@author: mark
'''


import webapp2
from envdef import Handler
from dbfunc import getQuestion, createQuestion, updateRating, voteQuestion
from secrets import testCookieHash, makeCookieHash
import logging

HTML_TEMPLATE = "question.html"

      
class AjaxHandler(Handler):
    def get(self):
        genre = self.request.cookies.get('genre')
        qD = getQuestion(genre)
        qRating = qD['rating']
        self.setCookie('qRating', qRating)#secure with hash of answer or something later.
        qK = qD['key']
        self.setCookie('qK', str(qK))
        self.render(HTML_TEMPLATE, **qD)
        
    def post(self):
        ######################################
        #case: create question
        q = self.request.get('q')
        a = self.request.get('a')
        c1= self.request.get('c1')
        c2= self.request.get('c2')
        c3= self.request.get('c3')
        genre= self.request.get('genreSet')
        logging.info("genre is: " + genre)
        if q and a and c1 and c2 and c3 and genre:
            createQuestion(q,a,c1,c2,c3, genre)
            return
        ######################################
        #case: grade question
        ans = self.request.get('ans')
        hashed = self.request.get('hashed')
        if ans and hashed:
            if testCookieHash(hashed,ans):
                self.response.out.write('<div style="color:green">That\'s correct!</div>')
                score = 1
            else:
                self.response.out.write('<div style="color:red">Nope sorry.</div>')
                score = 0
            userName = self.testCookie('user')
            userRating = str(self.testCookie('rating'))[len(userName):]
            qK = self.testCookie('qK')
            qRating = self.testCookie('qRating')
            userRating = updateRating(userName, float(userRating), qK, float(qRating), score)
            self.setCookie('rating', userName + userRating)
            return
        #case: good question vote
        good = self.request.get('good')
        if good:
            qK = self.testCookie('qK')
            voteQuestion(1,qK)
            return
        bad = self.request.get('bad')
        if bad:
            qK = self.testCookie('qK')
            voteQuestion(0,qK)
            return
            

app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

