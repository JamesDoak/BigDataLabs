from pymongo import MongoClient

client = MongoClient()
 
restaurants = client.test.restaurants
movies = client.test.movieDetails


#################################
## Task 3 - question 3
for restaurant  in restaurants.find( { "borough":"Queens", "cuisine" : "Delicatessen" } ):
    print(restaurant['name'] + " --- " + restaurant['address']['street'])


	
#############################
## Task 3 - question 4
# using query document only
for movie in movies.find({"director": "Sergio Leone"}):
    print('\n', movie['title'] + ",  Wins: " + str(movie['awards']['wins']) +  \
    ",  Nominations: " + str(movie['awards']['nominations']) + \
    ", Text: " + movie['awards']['text'])

# using query document and projection document
for movie in movies.find({"director": "Sergio Leone"}, {'title': 1,  'awards':1, 'director':1}):
    print ('\n', movie['title'] + ",  Wins: " + str(movie['awards']['wins']) +  \
    ",  Nominations: " + str(movie['awards']['nominations']) + \
    ", Text: " + movie['awards']['text'])


	
################################
## Task 3 - question 5
import datetime

newgrade = { \
            "date" : datetime.datetime.now(),
            "grade" : "B",
            "score" : 15
            }


restaurants.update_one( {'name': "Line Bagels"},  \
                    {'$push': {'grade': newgrade}} )

print('\n', restaurants.find_one({'name': "Line Bagels"}))
