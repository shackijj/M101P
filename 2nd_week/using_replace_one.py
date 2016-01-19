#!/usr/bin/python

import pymongo
import sys
import datetime

connection = pymongo.MongoClient("mongodb://localhost")

def remove_all_review_dates():

    db = connection.school
    scores = db.scores

    print "\n\nremoving all review dates..."

    try:
        result = scores.update_many({'review_date':{'$exists':True}},
                                    {'$unset':{'review_date':1}})
        print "Matched this number of docs: ", result.matched_count

    except Exception as e:
        raise

def add_review_date_using_replace_one(student_id):
    
    db = connection.school
    scores = db.scores

    print "updating record using update one"

    try:
        score = scores.find_one({'student_id':student_id,
                                 'type':'homework'})
        print "before: ", score
        score['review_date'] = datetime.datetime.utcnow()
        
        record_id = score['_id']
        scores.replace_one({'_id':record_id}, score)
        score = scores.find_one({'_id': record_id})
        print "after: ", score        

    except Exception as e:
        raise

remove_all_review_dates()
add_review_date_using_replace_one(1)
