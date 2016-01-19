import pymongo

from pymongo import MongoClient

#connect to db

connection = MongoClient('localhost', 27017)

db = connection.test

names = db.names

item = names.find_one()

print item['name']
