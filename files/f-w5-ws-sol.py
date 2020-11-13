# Map, Filter, Reduce
#1. minutesToHours(l): convert a list of minutes into a list of hours.

def minutesToHours(l):
    return list(map(lambda x: x/60, l)) 


#2. nonnegative(l): given a list of integers, return the original list 
# but with all negative numbers replaced by 0.

def nonnegative(l): 
    return list(map(lambda x: 0 if x < 0 else x, l))


#3. punctuation(l): given a list of strings, remove all strings that end 
# in '?' but add '!' to the end of all other strings.
# e.g. ['hello?', 'world'] --> ['world!']

def punctuation(l):
    strNotQuest = list(filter(lambda x: x[len(x)-1]!="?", l))
    return list(map(lambda x: x+"!", strNotQuest))


#4. Write a function average(l) that takes a non-empty list of numbers
# and returns their average.
# Note: avoid using sum() function. 

def average(l):
    return reduce(lambda x,y: x+y, l) / len(l)


#5. Professor Pennypincher will not buy anything if he has to pay more
# than 200 dollars. But, as a member of the Generous Teachers Society, he 
# gets a 10% discount on anything he buys. Write a function pennypincher 
# that takes a list of prices and returns the total amount that Professor 
# Pennypincher would have to pay, if he bought everything that was cheap 
# enough for him. For example, pennypincher([100, 150, 200, 210, 250]) 
# returns 594.0.

def pennypincher(l):
    discounted = list(map(lambda x: x * 0.9, l))
    cheapEnough = list(filter(lambda x: x <= 200, discounted))
    return reduce(lambda x,y: x+y, cheapEnough)


#6.  Professor Puzzler is a crossword enthusiast. He has a long list of 
# words that might appear in a crossword puzzle, but he has trouble 
# finding the ones that fit a slot. Write a function crosswordFind to 
# help him. The expression crosswordFind(letter, inPosition, length, words)
# should return all the items from the list words which (1) are of the 
# given length and (2) have letter in the position inPosition.
# For example, if Puzzler is looking for seven-letter words that have 'k' 
# in position 1, he can evaluate the expression:  
# crosswordFind('k', 1, 7, ["funky", "fabulous", "kite", "icky", "ukelele"]) 
# which returns ["ukelele"].

def crosswordFind(letter, position, length, wordList):
    return list(filter(lambda w : len(w) == length and position >= 0
                       and position < len(w) and w[position] == letter, wordList))

