#!/usr/bin/python

import pymongo
import sys
import datetime

connection = pymongo.MongoClient("mongodb://localhost")

def remove_student(student_id):
    db = connection.school
    scores = db.scores

    try:
        result = scores.delete_one({'student_id':student_id})
        print "num removed: ", result.deleted_count

    except Exception as e:
        print "Exception: ", type(e), e

def find_student_data(student_id):
    db = connection.school
    scores = db.scores
    print "Searching for student data for student id = ", student_id

    try:
        docs = scores.find({'student_id':student_id})
        for doc in docs:
            print doc

    except Exception as e:
        print "Exception: ", type(e), e

remove_student(1)
find_student_data(1)
