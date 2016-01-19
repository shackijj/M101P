#!/usr/bin/python

import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

def insert_many():

    db = connection.school
    people = db.people

    print "insert, reporting for duty"

    richard = {"name":"Richard Kreuter", "company":"10gen",
               "interests":['horses', 'skydiving','fencing']}

    andrew =  {"_id":"erlichson","name":"Andrew Erlichson",
               "company":"10gen", 
               "interests":['running','cycling','photography']}

    people_to_insert = [andrew, richard]

    try:
        people.insert_many(people_to_insert, ordered=False)
    except Exception as e:
        print "Unhandled exception:", type(e), e

    print richard
    print andrew

def print_people():

    db = connection.school
    people = db.people

    cur = people.find({}, {'name':1})
    for doc in cur:
        print doc

print "Before the insert_many, here are people"
print_people()
insert_many()
print "\n\nAfter insert many, here are people"
print_people()
