'''
Created on Dec 2, 2012

@author: mark

In case you were wondering, all of these values SHOULD BE CHANGED 
BEFORE PUTTING ONLINE.

'''
import hashlib

#if you change this part after storing values with them you lose those values
#a five char secret
salt5 = "tIqwP"
#a ten char secret
salt10 = "uBrtVlKAcX"


#Definately case-sensitive. lower() will change that but denies users hoped for security 
#if you change this part after storing values with them you lose those values
def makeHash(raw):
    return hashlib.sha256(salt5 + raw + salt10).hexdigest()
    
def testHash(t_hash, raw):
    test = hashlib.sha256(salt5 + raw + salt10).hexdigest()
    if t_hash == test:
        return True
    else:
        return False

salt8 ="TuFGhoIl"
salt11 ="RRstigyQxMb"

def makeCookieHash(raw):
    return hashlib.sha256(salt8 + str(raw) + salt11).hexdigest()
def testCookieHash(t_hash, raw):
    test = hashlib.sha256(salt8 + str(raw) + salt11).hexdigest()
    if t_hash == test:
        return True
    else:
        return False
    
