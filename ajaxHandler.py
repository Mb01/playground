'''
Created on Dec 29, 2012

@author: mark
'''

import random
import webapp2
from envdef import Handler
from dbfunc import getQuestions

HTML_TEMPLATE = "mainpage.html"

def questionForm():
    questions = getQuestions()
    if not questions:
        return "Couldn't get a question."
    q  = random.choice(questions)
    
    data_out = q['question']
    
        

class AjaxHandler(Handler):
    def get(self):
        #lets just get it to the point where it can return a question
        data_out = questionForm()
        self.response.out.write(data_out)
        
    def post(self):
        pass
        #self.response.out.write(data_out)

app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

