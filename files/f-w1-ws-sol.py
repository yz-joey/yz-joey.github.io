# 1. Implement the function 'square' that takes an input and returns the square
# of the input.
#    Example: input: 2
#             return value: 4
def square(input):
	return 0

# 2. Implement a function differenceOfSquares that takes two input numbers and
# returns the difference of their squares. Make use of square function that you
# have already written.
# Example: input : n1 = 3, n2 = 2
#          return value : 5
def differenceOfSquares(n1, n2):
	return 0

# 3. Implement function simpleInterest that takes as input principle p, rate r
# (in %) and time t and returns the interest value.
#   Example In : p = 3100.00, r = 7, t =1
#           Out : 'Simple Interest = 217.00'
#   Hint : Please lookup the formula for simple interest
def simpleInterest(p, r, t):
	return 0.0

# 4. In digital electronics, a NAND gate (NOT-AND) is a logic gate which
# produces an output which is False if and only if all its inputs are True.
# Implement the 'nand' function using the 'and', 'or', and 'not' built-in
# Python functions.
# Example:
#        nand(True, False) outputs True
#        nand(False, False) outputs True
#        nand(True, True) outputs False
def nand(a, b):
	return False


# 5. Write a function checkends(s), which takes in a string s and returns True
# if and only if the first character in s is the same as the last character in
# s. The checkends function does not have to work on the empty string (the
# string '').
# Example: In: s = 'hah! a match'
#          Out: True
#          In: s = 'not a match'
#          Out: False
def checkends(s):
	# assume s is not empty
	return False

# 6. Write the function palindrome(s) that checks if a string of exactly length
# 4 is a palindrome (the same forwards as it is when the order is reversed).
# Example: In: s = 'lool'
#          Out: True
#          In: "UCLA"
#          Out: False
# Please use your checkends function.
def palindrome(s):
	# assume s has length 4
	return False


# 7. Write convertFromSeconds(s), which takes in a nonnegative integer number
# of seconds s and returns a list (we'll call it L) of four nonnegative
# integers that represents that number of seconds in more conventional units of
# time, such that:
# L[0] element represents the number of days
# L[1] represents the number of hours
# L[2] represents the number of minutes
# L[3] represents the number of seconds
# Example: In: s = 99999
#          Out: [1, 3, 46, 39]
#
# For this problem you will need both the modulo operator '%' (which we saw in
# class) and the new "floor division" operator '//'. The floor division
# 'a // b' gives us the greatest integer k such that b*k <= a. For instance,
# 12 // 5 = 2 because 2*5 < 12, but 3*5 > 12. Play with this operator to get a feel
# for it.
def convertFromSeconds(s):
	days =  
	hours = 
	minutes = 
	seconds = 
	return [days, hours, minutes, seconds]


