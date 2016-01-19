#!/usr/bin/python

import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

def insert():

    db = connection.school
    people = db.people

    print "insert, reporting for duty"

    richard = {"name":"Richard Kreuter", "company":"10gen",
               "interests":['horses', 'skydiving','fencing']}

    andrew =  {"_id":"erlichson","name":"Andrew Erlichson",
               "company":"10gen", 
               "interests":['running','cycling','photography']}

    try:
        people.insert_one(richard)
        people.insert_one(andrew)
    except Exception as e:
        print "Unhandled exception:", type(e), e

    print richard
    print andrew

insert()
