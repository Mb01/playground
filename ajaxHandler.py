'''
Created on Dec 29, 2012

@author: mark
'''

import random
import webapp2
from envdef import Handler
from dbfunc import getQuestions

HTML_TEMPLATE = "question.html"

def questionForm():
    questions = getQuestions()
    if not questions:
        return "Couldn't get a question."
    q  = random.choice(questions)
    return q
        

class AjaxHandler(Handler):
    def get(self):
        
        
        self.render(HTML_TEMPLATE, **questionForm())
        
    def post(self):
        pass

app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

