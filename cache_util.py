'''
Created on Dec 1, 2012

@author: mark

wrap memcache
'''

from google.appengine.api import memcache

def mems(key,val):
    '''cache set'''
    memcache.set(key, val) #@UndefinedVariable works though

def memg(key):
    '''cache get'''
    return memcache.get(key) #@UndefinedVariable works though
