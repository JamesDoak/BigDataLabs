from pymongo import MongoClient
import datetime

#Step 1: create a MongoClient 
client = MongoClient()
blogs =client.test.blogs

#Step 2: Create sample documents 
document = {
            "title" : "How I Learned MongoDB",
            "author" : "Slade Cozart",
            "date" : datetime.datetime(2013, 11, 14),
            "tag" : ["MongoDB", "Database", "ObjectRocket"],
            }

more_documents =[ {
                  "title" : "Reflections on 10 Years of MongoDB",
                  "author" : "Eliot Horowitzc",
                  "date" : datetime.datetime(2017, 10, 19),
                  "tag" : ["MongoDB", "Database", "NoSQL"]
                  },
                  {
                  "title" : "MongoDB 3.6.0-rc0 is released",
                  "author" : "MongoDB Inc",
                  "date" : datetime.datetime(2017, 10, 20),
                  "tag" : ["MongoDB", "founder"]
                   }]
 
#Step 3: Insert sample document object directly into MongoDB, 
#and Print to the console the ObjectID of the new document
print(blogs.insert(document))
print(blogs.insert(more_documents))
