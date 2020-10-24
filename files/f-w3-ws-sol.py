# 1. Write a function named tails that takes a list and returns a list of 
# lists containing the original list along with all tails of the list, from 
# longest to shortest.  For example, tails([1,2,3]) is [[1,2,3], [2,3], [3], []],
# and tails([]) = [[]].
def tails(l):
	if l == []: 
		return [[]] # not return []
	else:
		t = l[1:]
		return [l] + tails(t)

# tails(t) = [[2,3], [3], []]
# target = [[1,2,3], [2,3], [3], []]
# target = missing + tails[t]
# missing = [[1,2,3]] = [l]
# [[1,2,3], [2,3], [3], []] = [[1,2,3], [2,3], [3]] + [[]]

# 2. Write a function named flatten that takes a list of lists and flattens it 
# into a single list.  For example, flatten([[1,2], [3], [], [4,5,6]]) returns 
# [1,2,3,4,5,6].
def flatten(l):
	if l == []:
		return []
	else:
		return l[0] + flatten(l[1:])


# 3. Write a function named rmDups that removes consecutive duplicates from a 
# list. For example, rmDups([1,2,2,3,3,3,4,2,2,3]) returns [1, 2, 3, 4, 2, 3].
def rmDups(l):
	if len(l) < 2:
		return l
	elif l[0] == l[1]:
		return rmDups([l[0]] + l[2:])
	else:
		return [l[0]] + rmDups(l[1:])


# 4. Write a function named q that checks that every number in a list that is 
# between 10 and 100 (inclusive) is even.  For example, q([1,10,153,84,64,9]) 
# returns False.
def q(l):
	if l == []:
		return True
	else:
		if 10 <= l[0] <= 100 and l[0] % 2 != 0:
			return False # and q(l[1:])
		else:
			return q(l[1:])

# true and true and true and true --> true
# true and true and false and true --> false

#sol2 using a flag to record the true/false status before the current checking 
def q(l):
	return helper(l, True)

def helper(l, flag):
	if l == []:
		return flag
	else:
		if 10 <= l[0] <= 100 and l[0] % 2 != 0:
			return helper(l[1:], False)
		else:
			return helper(l[1:], True)		


# 5. Write a function named minimum that returns the smallest element in a list 
# of integers.  You may assume the list is non-empty.
def minimum(l):
	return helper(l, l[0])

def helper(l, min_num):
	if l == []:
		return min_num
	else:
		if l[0] < min_num:
			return helper(l[1:], l[0])
		else:
			return helper(l[1:], min_num)


# 6. I live pretty close to campus. Every morning I use the Python function below 
# to determine what mode of transportation to use to commute to work, based on how 
# many hours of sleep I got the previous night (argument sleep) and how many minutes 
# I have before my first meeting of the day (argument minutesForTravel).
def commute(sleep, minutesForTravel):
	if sleep < 7:
		return "car"
	elif minutesForTravel >= 60:
		return "walk"
	elif minutesForTravel >= 30:
		return "bike"
	else:
		return "car"

# (a) What is my mode of transportation when I’ve gotten 8 hours of sleep and have 
# 45 minutes until my first meeting?
sol:"bike"

# (b) Show a call to commute that returns the result "walk".
sol:commute(8, 60)

# (c) According to the commute function, under what conditions do I drive my car to campus?
# (Choose the single best answer.)
# i. when I’ve gotten fewer than 7 hours of sleep
# ii. when I have fewer than 30 minutes until my first meeting
# iii. when both of i and ii above are true
# iv. when at least one of i and ii above is true
# v. when exactly one of i and ii above is true
sol:iv


# 7. Consider this function, where l is a list:
def mystery(l):
	if l == []:
		return []
	else:
		head = l[0]
		tail = l[1:]
	return mystery(tail) + [head]

# (a) What does mystery([1,3,5]) return?
sol:[5,3,1]

# (b) How many times is mystery called during the execution of mystery([1,3,5]), 
# including the initial call to mystery?
sol:4

# (c) What are the first two lists to be concatenated (using the + operator) 
# during the execution of mystery([1,3,5])? Make sure that your answer preserves 
# the order of the two arguments to the concatenation operation.
sol:[] and [5]


# 8. Consider the following function where x,y,z are numbers
def secret(x,y,z):
	if (x + y) > z:
		return x + y
	elif (x + z) > y:
		return x + z
	else:
		return z
# (a) What is the result of secret(2,5,6)
sol:7

# (b) What is the result of secret((3+5),1,7)
# (i) 8
# (ii) 15
# (iii) 7
# (iv) 9
sol:(iv)


# 9. Consider the following functions where inp is a number and lst that is a list
def posQuadraple(inp):
	if inp > 0:
		return inp * 4
	else:
		return -1 * inp * 4

def greaterOfTwo(lst):
	if lst[0] > lst[1]:
		return lst[0]
	else:
		return lst[1]

# (a) What is the result of posQuadraple(greaterOfTwo ([-1,-2]))
sol:4

# (b) What is the result of posQuadraple(pow(greaterOfTwo([5,3]), 2))
sol:100


# 10. The federal income tax plan currently being considered in Congress imposes 
# a 12% tax on the first $37,500 of a person’s income, a 25% tax on all income 
# above $37,500 and less than or equal to $112,500, and a 35% tax on all income 
# above $112,500. For example, someone earning $30,000 would owe 
# 30,000 * 0.12 = $3600 in taxes, while someone earning $40,000 would owe 
# (37,500 * 0.12) + (2500 * 0.25) = $5125 in taxes. 
# Implement the function taxes that is declared below, which takes an income 
# (a number) as an argument and returns the taxes owed.
def taxes(income):
	if income <= 37500:
		return income * 0.12
	elif income <= 112500:
		return 37500 * 0.12 + (income - 37500) * 0.25
	else:
		return 37500 * 0.12 + (112500 - 37500) * 0.25 + (income - 112500) * 0.35 


# 11. You’ve been asked to implement a mini-calculator. The operators allowed 
# are +,-,*,/,%. . Implement a function miniCalculator that is declared below, 
# which two values x and y and a string operator op and returns the result of 
# x op y. e.g miniCalculator(3,1,’+’) returns 4.
def miniCalculator(x,y,op):
	if op == "+":
		return x + y
	elif op == "-":
		return x - y
	elif op == "*":
		return x * y
	elif op == "/":
		return x / y
	elif op == '%':
		return x % y
	else:
		return "Unsupported operator"
