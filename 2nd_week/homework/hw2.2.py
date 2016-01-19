#!/usr/bin/python

import pymongo

def remove_the_worst_homework():

    conn = pymongo.MongoClient("mongodb://localhost")

    db = conn.students
    grades = db.grades

    student_ids = grades.distinct("student_id")

    for student_id in student_ids:
        worst_homework = grades.find_one_and_delete(
            {'student_id':student_id,
             'type':'homework'},
             sort=[('score', pymongo.ASCENDING)]
        )

remove_the_worst_homework()
