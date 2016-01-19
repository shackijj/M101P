import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Kirill', 'lastname':'Shatsky'}

print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "Fisrt insert failed: %s", e

print doc
print "inserting again"

doc = {'firstname':'Kirill', 'lastname':'Shatsky'}

try:
    users.insert_one(doc)
except Exception as e:
    print "Second insert failed: %s", e


print doc
