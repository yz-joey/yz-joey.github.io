# 1. The function `everyOther(l)` takes as an argument a list `l` 
# and returns the second, fourth, sixth, etc. elements of `l`.
# Example: everyOther([1, 2, 3, 4]) == [2, 4].
#(1)
def everyOther(l):
	if len(l) <= 1:
		return []
	else:
		head = l[:2]
		tail = l[2:]
		return [head[1]] + everyOther(tail) 

#(2)
def everyOtherHelper(l, isSkipped):
	if l == []:
		return []
	else:
		head = l[0]
		tail = l[1:]
		if isSkipped:
			return everyOtherHelper(tail, not isSkipped) # not isSkipped == False
		else:
			return [head] + everyOtherHelper(tail, not isSkipped) # not isSkipped == True

def everyOther(l):
	return everyOtherHelper(l, True)


# 2. The function `isPalindrome(s)` returns True if and only if `s` is a palindrome, i.e.
# the same forwards as it is reversed.
# Example: isPalindrome("racecar") == True, isPalindrome("UCLA") == False
def isPalindrome(s):
	if len(s) == 0:
		return True
	else:
		head = s[0] # r
		tail = s[-1] # r
		mid = s[1:-1] # aceca
		#-------------------
		#(1)
		if head == tail: 
			return True and isPalindrome(mid)
		else:
			return False
		#(2)
		return head == tail and isPalindrome(mid)
		#--------------------

# 3. The function `getDigits(n)` returns a list of all the digits of `n`. 
# Assume that n >= 0.
# Hint: Recall the flooring division function "//" and "%".
# Example: getDigits(123) = [1, 2, 3], getDigits(0) = [0]
def getDigits(n):
	#---------------
	#(1)
	if len(str(n)) == 1:
		return [n]
	#(2)
	if n < 10:
		return [n]
	#(3) not perfect
	if n == 0:
		return [] # supposed to return [0] if input is 0
	#----------------
	else:
		head = n % 10 #I 3 #II 2
		tail = n // 10 #I 12 #II 1
		return getDigits(tail) + [head] #I [1, 2] + [3] #II [1] + [2]
	

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
def removeSmallestHelper(l, smallest):
	if l == []:
		return []
	else:
		head = l[0]
		tail = l[1:]
		if head == smallest:
			return tail
		else:
			return [head] + removeSmallestHelper(tail, smallest)


def removeSmallest(l):
	if len(l) == 0:
		return l
	else:
		smallest = minlist(l)
		return removeSmallestHelper(l, smallest)

# 5. The function `selectionSort(l)` returns the list `l` sorted from least to greatest.
# Your solution *must* make use of the `removeSmallest` function.
# Examples:
# selectionSort([1, 3, 5, -1, 0]) == [-1, 0, 1, 3, 5]
# selectionSort([1, 2, 3, 1, 3, 1]) == [1, 1, 1, 2, 3, 3] 
def selectionSort(l):
	if l == []:
		return []
	else:
		minimum = minlist(l)
		removed = removeSmallest(l)
		return [minimum] + selectionSort(removed)

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
	if l == []:
		return []
	elif type(l) == list:
		head = l[0]
		tail = l[1:]
		return flatten(head) + flatten(tail)
	else:
		return [l]