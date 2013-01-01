'''
Created on Dec 29, 2012

@author: mark
'''
import logging
import random
import webapp2
from envdef import Handler
from dbfunc import getQuestions, createQuestion

HTML_TEMPLATE = "question.html"

def questionForm():
    questions = getQuestions()
    if not questions:
        return "Couldn't get a question."
    q  = random.choice(questions)
    logging.info(q)
    
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
        createQuestion(q,a,c1,c2,c3)

app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

