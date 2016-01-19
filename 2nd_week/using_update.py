#!/usr/bin/python

import pymongo
import sys
import datetime

connection = pymongo.MongoClient("mongodb://localhost")

def add_review_date_using_update_one(student_id):

    db = connection.school
    scores = db.scores

    print "updating record, reporting for duty"

    try:
        score = scores.find_one({'student_id':student_id,
                                 'type':'homework'})
        print "before: ", score
        record_id = score['_id']
        result = scores.update_one({'_id':record_id},
            {'$set':{'review_date':datetime.datetime.utcnow()}})

        print "num mathced: ", result.matched_count

        score = scores.find_one({'_id':record_id})

        print "after: ", score

    except Exception as e:
        raise

def add_review_dates_for_all():
    
    db = connection.school
    scores = db.scores

    try:
        result = scores = scores.update_many({},
            {'$set' : {'review_date' : datetime.datetime.utcnow()}})
        print "num matched: ", result.matched_count

    except Exception as e:
        raise


#add_review_date_using_update_one(1)
add_review_dates_for_all()
