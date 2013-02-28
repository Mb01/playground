'''
Created on Dec 29, 2012

@author: mark
'''


import webapp2
from envdef import Handler
#from dbfunc import 
from secrets import testCookieHash, makeCookieHash
#import logging

HTML_TEMPLATE = "question.html"

      
class AjaxHandler(Handler):
    def get(self):
        pass


        
    def post(self):
        pass
        
                    

app = webapp2.WSGIApplication([('/ajax', AjaxHandler)], debug=True)

