import functools

# Video games often track player attributes using something like a dictionary.
# A *player map* p is a dictionary that has the following entries:
#   p["score"]: the current player's score, a non-negative integer
#   p["location"]: the player's location,
#           given as a dictionary with entries for "x" and "y" coordinates that are both integers.
#   p["health"]: the player's health, given as an integer between 0 and 100
#   p["name"]: the player's name, given as a string.
# For instance, an example player map is:
#  joeBruin = {"score": 1000, "location": {"x": 0, "y": -10}, "health": 50, "name": "Joe Bruin"}

# 1. Write a function that greets the player by printing "Hello, {player name}!"
#    (replace {player name} with their name) if they are alive (health
#    greater than 0), or prints "You are Dead!" if they are dead.
# Example: greetPlayer(joeBruin) prints "Hello, Joe Bruin!" to the console.
def greetPlayer(p):
    return

# 2. Write a function movePlayer(p, x, y) that returns a new player that is
# equivalent to the old one except at the new position (x, y), where x and y
# are both integer arguments.
# Example: movePlayer(joeBruin, 10, 10) == {'name': 'Joe Bruin', 'location': {'x': 10, 'y': 10}, 'health': 50, 'score': 1000}
def movePlayer(p, x, y):
    return

# Consider the following list of search results retrieved when looking up
# how to make a Thanksgiving dinner:
searchResults = [
    {"title": "The Perfect Cranberry Sauce", "keywords": ["cranberries"], "relevance": 25},
    {"title": "Roasting a Turkey: 101", "keywords": ["bird"], "relevance": 88},
    {"title": "How Not to Ruin Thanksgiving", "keywords": ["social gathering", "thanksgiving"], "relevance": 25},
    {"title": "How to Bake a Pie", "keywords": ["baking", "pie"], "relevance": 9},
    {"title": "One Hundred Things Your Uncle Shouldn't Say at Thanksgiving",
     "keywords": ["inappropriate behavior", "thanksgiving"], "relevance": 1},
    {"title": "How To Stuff a Turkey", "keywords": ["turkey", "stuffing", "baking advice"], "relevance": 88},
]

# Write functions that use map, filter, and reduce to compute the following
# quantities (where the list of search results is given as an argument). You
# can use the above list of search results as a test case, but feel free to
# modify it to get more tests.

# 3. Find the highest relevancy score in the search results.
# Example: findGreatestRelevance(searchResults) == 88
def findGreatestRelevance(results):
    return

# 4. Return the list of the title of all the search results with the greatest relevance.
# Example: findNamesOfGreatestRelevance(searchResults) == ["Roasting a Turkey: 101", "How To Stuff a Turkey"]
def findNamesOfGreatestRelevance(results):
    return

# 5. Find the list of titles of the most relevant search result with
# "thanksgiving" as a keyword.
# Example: mostRelevantWithThanksgiving(results) == ["How Not to Ruin Thanksgiving"]
def mostRelevantWithThanksgiving(results):
    return

# 6. Return the average length of the titles of all article with relevance at least
# as great as some constant k (given as an argument).
# Example: averageLengthAbovek(searchResults, 0) == 29.0
def averageLengthAbovek(results, k):
    return

