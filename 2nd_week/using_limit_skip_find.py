#!/usr/bin/python

import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores

def find():
    print "find, reporting fot duty"
    query = {}

    try:
        #cursor = scores.find(query).sort('student_id', pymongo.ASCENDING).skip(4).limit(5)
        cursor = scores.find(query).skip(4)
        cursor = cursor.limit(1)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING),
                              ('score', pymongo.DESCENDING)])

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
