'''
Created on Dec 29, 2012

@author: mark
'''

import webapp2
from envdef import Handler
from dbfunc import getQuestions

HTML_TEMPLATE = "mainpage.html"

class AjaxHandler(Handler):
    def get(self):
        #lets just get it to the point where it can return a question
        questions = getQuestions
        self.response.out.write(data_out)
    def post(self):
        self.response.out.write(data_out)
        
app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

