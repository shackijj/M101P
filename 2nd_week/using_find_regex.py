#!/usr/bin/python

import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.reddit
stories = db.stories

def find():
    print "find, reporting fot duty"
    query = {'title' : { '$regex' : 'amd|ssd', '$options' : 'i'}}
    projection = {'title' : 1, '_id' : 0}

    try:
        cursor = stories.find(query, projection)

    except Exception as e:
        print "Unexpected error: ", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break

find()
