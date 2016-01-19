#!/usr/bin/python

import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores

def find():
    print "find, reporting fot duty"
    query = {'type' : 'exam'}
    projection = {'student_id' : 1, '_id' : 0}

    try:
        cursor = scores.find(query, projection)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break

def find_one():
    print "find one, reporting for duty"
    query = {'student_id' : 10}
    
    try:
        doc = scores.find_one(query)
  
    except Exception as e:
        print "Unexpected error:" , type(e), e

    print doc

find()
