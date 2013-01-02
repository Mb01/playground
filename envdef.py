'''
Created on Dec 1, 2012

@author: mark
'''
import os
import webapp2
import jinja2
from secrets import makeCookieHash, testCookieHash

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Handler(webapp2.RequestHandler):
    """Extends request handler with custom functions"""
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
    def setCookie(self, name, value):
        '''set a cookie with a value and a hash of the value'''
        #get the value back with testCookie(name)
        cookieVal = "%s:%s" % (str(value), str(makeCookieHash(value)))
        self.response.set_cookie(name, cookieVal)
    
    def testCookie(self, name):
        '''tests a cookie against it's hash and return value if valid'''
        #create the cookie with setCookie
        cookie = self.request.cookies.get(name)
        if cookie and cookie.find(":") != -1:
            value, t_hash = cookie.split(':')
            if testCookieHash(t_hash, value):
                return value
        return False
    
    
    
    