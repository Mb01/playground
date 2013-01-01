'''
Created on Dec 29, 2012

@author: mark
'''
import logging
import random
import webapp2
from envdef import Handler
from dbfunc import getQuestions, createQuestion
from secrets import testCookieHash, makeCookieHash

HTML_TEMPLATE = "question.html"

def questionForm():
    questions = getQuestions()
    if not questions:
        return "Couldn't get a question."
    q  = random.choice(questions)
    options = [q['answer'], q['choice1'], q['choice2'], q['choice3']]    
    random.shuffle(options)
    q['options'] = options
    q['hashed'] = makeCookieHash(q['answer'])
    return q
        
class AjaxHandler(Handler):
    def get(self):
        self.render(HTML_TEMPLATE, **questionForm())
        
    def post(self):
        q = self.request.get('q')
        a = self.request.get('a')
        c1= self.request.get('c1')
        c2= self.request.get('c2')
        c3= self.request.get('c3')
        if q and a and c1 and c2 and c3:
            createQuestion(q,a,c1,c2,c3)
            return
        ans = self.request.get('ans')
        hashed = self.request.get('hashed')
        if ans and hashed:
            if testCookieHash(hashed,ans):
                self.response.out.write('<div style="color:green">That\'s correct!</div>')
            else:
                self.response.out.write('<div style="color:red">Nope sorry.</div>')
            

app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

