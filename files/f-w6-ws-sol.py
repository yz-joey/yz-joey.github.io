from functools import reduce

### Section1. use map/reduce/filter to solve the 1-5 questions. ###


#1. doubleLargeStrings(l): given a list of strings, retain only the ones 
# that have length at least 5 and repeat the string twice. 
# Example: ['hello','world','!'] --> [['hello','hello'],['world','world']]

def doubleLargeStrings(l): 
    lenAtleast5 = list(filter(lambda x: len(x) >= 5, l))
    return list(map(lambda x: [x, x], lenAtleast5))



#2.1 Write a function noZeroLists that takes a list of lists and
# removes any inner lists that contain at least one 0 in them.
# Example: noZeroLists_2([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
# returns [[1,2,3], [], [1,1,1]].
# Hint: Python's "in" operator for checking whether a value is in a 
# list will be useful.

def noZeroLists(l):
    return list(filter(lambda x: 0 not in x, l))


#2.2 Implement the noZeroLists function again only with reduce.
def noZeroLists_2(l):
    return reduce(lambda res,x: res+[x] if 0 not in x else res, l, [])

# reduce(f, l, init)
# init is optional argument.
# e.g reduce(lambda x,y: x+y, [2,3,4], 1)
# 1 + 2
# 3 + 3
# 6 + 4 = 10

# e.g. noZeroLists_2([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
# [] + [[1,2,3]] = [[1,2,3]]
# [[1,2,3]]
# [[1,2,3]] + [[]] = [[1,2,3]]


#3. Write a function named count that takes an item e and a list l and 
# returns the number of occurrences of e in l.
# Note: please use only reduce to implement this function.
def count(e, l):
    return reduce(lambda res, x: res+1 if x == e else res, l, 0)



#4. Write a function innerMultiply that multiplies all elements of a 
# list of lists by a given number. For example, 
# innerMultiply([[1,2,3], [4,5]], 10) returns [[10,20,30], [40,50]].
# Hint: You'll need to use a map within a map!

def innerMultiply(l, n):
    return list(map(lambda x: list(map(lambda y: y*n, x)), l))

# nested map
# application: conduct transformation on list of list
# map(lambda x: map(lambda y: ...), l)
# map(f1, l)
# def f1(x):
#   return map(f2, x)
# def f2(y):
#   return ...


#5. Write a function named q that checks that every number in a list that 
# is between 10 and 100 (inclusive) is even.  
# Example, q([1,12,153,84,64,9]) returns True.

def q(l):
    inRange = list(filter(lambda x: x >= 10 and x <= 100, l))
    isEven = list(filter(lambda x: x % 2 == 0, inRange))
    return len(inRange) == len(isEven)

### Section2. use recursive functions to solve the following problems. ###


#6. Write a function named pairify that concatenate each two elements in a 
# list to a new list.  
# Note: we assume the length of the list is always even.
# Example: pairify([1,5,6,8,9,10]) -> [[1,5], [6,8], [9,10]] 

def pairify(l):
    if l == []:
        return []
    else:
        head = l[0:2]
        tail = l[2:]
    return [head] + pairify(tail)

# [[1,2,3]] + [] = [[1,2,3]]
# [[1,2,3]] + [[]] = [[1,2,3], []]

#7. Write a function named zip that takes two lists of the same length as 
# input,  and concatenate the elements from the same position of the two 
# lists to a new list. 
# Example1: zip([1,2,3], [4,5,6]) -> [[1,4], [2,5], [3,6]]
# Example2: zip([1], [4]) -> [[1, 4]]
# Example3: zip([], []) -> []

def zip(l1, l2):
    if len(l1) == 0:
        return []
    else:
        head = [l1[0], l2[0]]
        # head = [l1[0]] + [l2[0]]
        zippedTail = zip(l1[1:], l2[1:])
    return [head] + zippedTail


#8. *(challenge)* A *sublist* of a list l is a list one can form by removing
# zero or more elements from l: for instance, [1, 3] is a sublist of [1,2,3,4],
# since one can remove 2 and 4 from [1, 2, 3, 4] to form [1, 3]. By definition,
# both [] and l itself are always sublists of any list l.
# Implement allSublists(l) which, given a list l, returns
# list of all sublists one can form from l. The returned list can be in any order: all
# that matters is that it contains each sublist exactly once.
# Example: allsublists([1, 2, 3]) == [[], [1], [2], [3], [1,2], [1,3], [2, 3], [1, 2, 3]]
#          allsublists([1,1]) == [[], [1], [1], [1,1]]
# Hint: Be careful about your base case.

def allSublists(l):
    if l == []:
        return [[]]
    else:
        head = l[0]
        tail = l[1:]
        tailLists = allsublists(tail)
        withHead = list(map(lambda x : [head] + x, tailLists))
        return withHead + tailList


#9.*(challenge)* Implement unzip(l) function which is the inverse of zip. 
# Note: we assume every list in l contains same amount of elements. 
# Example: unzip([[1,4], [2,5], [3,6]]) -> [[1,2,3], [4,5,6]]

def unzip(l):
    if l == []:
        return [[], []]
    else:
        head = l[0]
        tail = l[1:]
        unzippedTail = unzip(tail)
        return [[head[0]] + unzippedTail[0], [head[1]] + unzippedTail[1]]







