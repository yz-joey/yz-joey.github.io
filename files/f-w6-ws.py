from functools import reduce

### Section1. use map/reduce/filter to solve the 1-5 questions. ###


#1. doubleLargeStrings(l): given a list of strings, retain only the ones 
# that have length at least 5 and repeat the string twice. 
# Example: ['hello','world','!'] --> [['hello','hello'],['world','world']]

def doubleLargeStrings(l): 
    return 



#2.1 Write a function noZeroLists that takes a list of lists and
# removes any inner lists that contain at least one 0 in them.
# Example: noZeroLists([[1,2,3], [4,0,5], [], [1,1,1], [0,1,2]])
# returns [[1,2,3], [], [1,1,1]].
# Hint: Python's "in" operator for checking whether a value is in a 
# list will be useful.

def noZeroLists(l):
    return 


#2.2 Implement the noZeroLists function again only with reduce.
def noZeroLists_2(l):
    return 



#3. Write a function named count that takes an item e and a list l and 
# returns the number of occurrences of e in l.
# Note: please use only reduce to implement this function.
def count(e, l):
    return 



#4. Write a function innerMultiply that multiplies all elements of a 
# list of lists by a given number. For example, 
# innerMultiply([[1,2,3], [4,5]], 10) returns [[10,20,30], [40,50]].
# Hint: You'll need to use a map within a map!

def innerMultiply(l, n):
    return 



#5. Write a function named q that checks that every number in a list that 
# is between 10 and 100 (inclusive) is even.  
# Example, q([1,12,153,84,64,9]) returns True.

def q(l):
    return 




### Section2. use recursive functions to solve the following problems. ###


#6. Write a function named pairify that concatenate each two elements in a 
# list to a new list.  
# Note: we assume the length of the list is always even.
# Example: pairify([1,5,6,8,9,10]) -> [[1,5], [6,8], [9,10]] 

def pairify(l):
    return 


#7. Write a function named zip that takes two lists of the same length as 
# input,  and concatenate the elements from the same position of the two 
# lists to a new list. 
# Example1: zip([1,2,3], [4,5,6]) -> [[1,4], [2,5], [3,6]]
# Example2: zip([1], [4]) -> [[1, 4]]
# Example3: zip([], []) -> []

def zip(l1, l2):
    return


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
    return



#9.*(challenge)* Implement unzip(l) function which is the inverse of zip. 
# Note: we assume every list in l contains same amount of elements. 
# Example: unzip([[1,4], [2,5], [3,6]]) -> [1,2,3], [4,5,6]

def unzip(l):
    return 







