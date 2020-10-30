# 1. The function `everyOther(l)` takes as an argument a list `l` 
# and returns the second, fourth, sixth, etc. elements of `l`.
# Example: everyOther([1, 2, 3, 4]) == [2, 4].
def everyOther(l):
	return False

# 2. The function `isPalindrome(s)` returns True if and only if `s` is a palindrome, i.e.
# the same forwards as it is reversed.
# Example: isPalindrome("racecar") == True, isPalindrome("UCLA") == False
def isPalindrome(s):
	return False


# 3. The function `getDigits(n)` returns a list of all the digits of `n`. 
# Assume that n >= 0.
# Hint: Recall the flooring division function "//".
# Example: getDigits(123) = [1, 2, 3], getDigits(0) = [0]
def getDigits(n):
	return 0

# Here is a useful helper function for the next two exercises.
# minlist(l) takes a non-empty list l and returns the minimum element from that list.
def minlist(l):
	if len(l) == 1:
		return l[0]
	else:
		head = l[0]
		tail = l[1:]
		minTail = minlist(tail)
		if head < minTail:
			return head
		else:
			return minTail

#4. The function `removeSmallest(l)` takes as an argument a list of integers `l` and 
# returns a list that is equal to `l` except that the minumum element is removed.
# If there are multiple minimum elements, remove the first one.
# Examples:
# removeSmallest([1, 2, 3]) == [2, 3]
# removeSmallest([8, -1, 0]) == [8, 0]
# removeSmallest([0]) == []
# removeSmallest([2, 3, 2, 3]) == [3, 2, 3]
def removeSmallest(l):
	return []

# 5. The function `selectionSort(l)` returns the list `l` sorted from least to greatest.
# Your solution *must* make use of the `removeSmallest` function.
# Examples:
# selectionSort([1, 3, 5, -1, 0]) == [-1, 0, 1, 3, 5]
# selectionSort([1, 2, 3, 1, 3, 1]) == [1, 1, 1, 2, 3, 3] 
def selectionSort(l):
	return []

# 6. (Challenge Question) Python lists can contain heterogeneous data. For instance, a list can contain sub-lists, like [1, [2, [3]]].
# Give a function `flatten(l)` that takes a heterogeneous list as an argument and returns a single list without any
# nested lists. Note that the original ordering should be preserved.
# Examples:
# flatten([1, [1, [2, 3]]]) = [1, 1, 2, 3]
# flatten([[1, 2], [2, 4]]) = [1, 2, 2, 4]
# flatten(1) = [1]
# flatten([]) = []
# 
# Hint: You can test if a variable `x` is a list by checking if its type is equal to `list`. For instance,
# if type(x) == list:
# 	# x is a list!
# else:
#   # x is not a list.
def flatten(l):
	return []