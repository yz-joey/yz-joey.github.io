#Separately solve each of these problems using recursion, loops, map/filter/reduce
#----

# 1. Write a function average that takes a non-empty list of numbers and returns their average.
#1. Using Recursion
def sumList(l):
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        tailSum = sumList(tail)
        return head + tailSum

def average_rec(l):
    return sumList(l)/len(l)

#1 Using Loops
def average_loops(l):
    accum = 0
    for x in l:
        accum = accum + x
    return accum/len(l)

#1 Using reduce
def average_red(l):
    return reduce(lambda x,y: x+y, l) / len(l)


# 2. Write a function noZeroLists that takes a list of lists and removes any
#    inner lists that contain at least one 0 in them.
#    For example, noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
#    returns [[1,2,3], [], [1,1,1]].
#    Hint: Python's "in" operator for checking whether a value is in a list will be useful.

#2 Using Recursion
def noZeroLists_rec(l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        tailRes = noZeroLists_rec(tail)
        if not 0 in head:
            return [head] + tailRes
        else:
            return tailRes

#2 Using loops
def noZeroLists_loops(l):
    accum = []
    for x in l:
        if not 0 in x:
            accum = accum + [x]
    return accum

#2 Using filter

def noZeroLists_filter(l):
    return list(filter(lambda il: not(0 in il), l))


#3. Professor Puzzler is a crossword enthusiast. He has a long list of words that might appear
#   in a crossword puzzle, but he has trouble finding the ones that fit a slot.
#   Write a function crosswordFind to help him.
#   The expression crosswordFind(letter, inPosition, length, words)
#   should return all the items from the list words which (a) are of the given length
#   and (b) have letter in the position inPosition.
#   For example, if Puzzler is looking for seven-letter words that have 'k' in position 1,
#   he can evaluate the expression:
#   crosswordFind('k', 1, 7, ["funky", "fabulous", "kite", "icky", "ukelele"])
#   which returns ["ukelele"].

#3 Using recursion
def crosswordFind_rec(letter, position, length, wordlist):
    if wordlist == []:
        return []
    else:
        head = wordlist[0]
        tail = wordlist[1:]
        tailRes = crosswordFind_rec(letter, position, length, tail)
        if len(head) == length and 0 <= position <= len(head)-1 and head[position] == letter:
            return [head] + tailRes
        else:
            return tailRes

#3 Using loops
def crosswordFind_loops(letter, position, length, wordlist):
    accum = []
    for x in wordlist:
        if len(x) == length and 0 <= position <= len(x)-1 and x[position] == letter:
            accum = accum + [x]
    return accum


#3. Using filter
def crosswordFind_filter(letter, position, length, wordList):
    return list(filter(lambda w : len(w) == length and 0 <= position <= len(x)-1 and w[position] == letter, wordList))

# Note: the compiler follows the order to check all the conditions.


# 4. Write a function innerMultiply that multiplies all elements of a list of lists
#    by a given number.  For example, innerMultiply([[1,2,3], [4,5]], 10)
#    returns [[10,20,30], [40,50]].  Hint: You'll need to use a map within a map!

#4 Using recursion
def multiplyList(l, n):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        tailRes = multiplyList(tail,n)
        return [head*n] + tailRes

def innerMultiply_rec(l,n):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        tailRes = innerMultiply_rec(tail,n)
        return [multiplyList(head,n)] + tailRes


#4 Using loops:
def innerMultiply_loops(l,n):
    accum = []
    for x in l:
        res = []
        for e in x:
            res = res + [e*n]
        accum = accum +[res]
    return accum

#4c. Using a functional tool (like map, reduce, or filter)
def innerMultiply_map(l, n):
    return list(map(lambda innerL: list(map(lambda m: m*n, innerL)), l))


# 5. Write a function named q that checks that every number in a list that is
#    between 10 and 100 (inclusive) is even.
#    For example, q([1,12,153,84,64,9]) returns True.

#5a. Using recursion
def q_rec(l):
    if l == []:
        return True
    else:
        head = l[0]
        tail = l[1:]
        tailRes = q_rec(tail)
        if head >= 10 and head <=100 and head % 2 != 0:
            return False
        else:
            return tailRes

#5b. Using loops
def q_loops(l):
    res = True
    for x in l:
        if x >=10 and x <= 100 and x%2 != 0:
            return False
    return res



#5c. Using a functional tool (like map, reduce, or filter)
def q_func(l):
    inRange = list(filter(lambda x: x >= 10 and x <= 100, l))
    isEven = list(filter(lambda x: x % 2 == 0, inRange))
    return len(inRange) == len(isEven)

################################################################################3
# Part 2: More Exercises


# Write the function doubleLast(l) that modifies l (a list of integers) in
# place to double its last element. Assume l is non-empty. doubleLast should
# return None (i.e., not return any values.)
# Example:
# x = [1, 2, 3]
# doubleLast(x)      <-- after this call, x should be [1, 2, 6]
def doubleLast(l):
    l[-1] = l[-1] * 2


# If we add a return here
def doubleLast_return(l):
    l[-1] = l[-1] * 2
    return l

l = [1,2,6]
l2 = doubleLast(l)

l2 == [1,2,12]
l == [1,2,12] 

l2[2] = 11
l == [1,2,11]
# l ----> [1,2,12] <----- l2
# l ----> [1,2,11] <----- l2

l2 = [1,2,10]
l == [1,2,11]
# l ----> [1,2,11]  
# l2 ----> [1,2,10]




# Sometimes people have a preferred name that they would rather use instead of
# their given name.
# Write a function greetPreferredName(givenNames, preferredName) that given a list of
# strings "givenNames" and dictionary "preferredName" that maps given names to preferred names,
# prints "Hello (preferred name)!" on a separate for each person. If there is no preferred name, simply
# greet with the given name.
# The function should return None, and should print the names in the order that they appear in the list.
# Example:
# greetPreferredName(["steven", "joey", "todd"], {"steven": "steve", "todd": "the toddster"}) prints:
# Hello steve!
# Hello joey!
# Hello the toddster!
def greetPreferredName(givenNames, preferredName):
    for name in givenNames:
        if name in preferredName:
            print("Hello " + preferredName[name] + "!")
        else:
            print("Hello " + name + "!")


# Write a function printOnce(l) that prints each element of the list on a
# separate line, while skipping duplicates. The elements should be printed
# in the order that they appear in the list.
# Example:
# printOnce([1, 3, 2, 1, 4, 2]) prints:
# 1
# 3
# 2
# 4
def printOnce(l):
    seen = {}
    for x in l:
        if x not in seen:
            seen[x] = 0
            print(x)


def printOnce_2(l):
    seen = []
    for x in l:
        if x not in seen:
            seen += [x]
            print(x)

# In dictionary, when you look for a key, it will first call a function to
# convert the key to an address and directly check if data was stored there.
# In list, when you look for a key, it will iterate over all the elements 
# and check if at least one of them equals to the target.
# Therefore, in terms of checking existence, dictionary is faster than list. 


# Write a function findMostFrequent(l) that finds the most frequent element in
# a list. Assume that there is a unique most common element.
# Example: findMostFrequent([1, "hello", 3, 3, 3, 1, 8, 4]) == 3
# Hint: remember the "tally" example from class.


def findMostFrequent(l):
    counter = {}
    maxCount = 0
    for x in l:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
    res = ""
    for x in l:
        if counter[x] >= maxCount:
            maxCount = counter[x]
            res = x
    return res

def findMostFrequent_seen(l):
    counter = {}
    seen = []
    maxCount = 0
    for x in l:
        if x not in counter:
            counter[x] = 1
            seen += [x]
        else:
            counter[x] += 1
    res = ""
    for x in seen:
        if counter[x] >= maxCount:
            maxCount = counter[x]
            res = x
    return res

def findMostFrequent_2(l):
    counter = {}
    maxCount = 0
    for x in l:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
    res = ""
    for x in counter:
        if counter[x] >= maxCount:
            maxCount = counter[x]
            res = x
    return res

def findMostFrequent_3(l):
    curMostCommon = 0
    greatestCount = 0
    d = {}
    for x in l:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
        curCount = d[x]
        if curCount > greatestCount:
            greatestCount = curCount
            curMostCommon = x
    return curMostCommon



