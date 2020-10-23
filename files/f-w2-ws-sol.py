# 1. compare two numbers and return the larger one.

def larger_between_two(a,b):
    if a > b:
    	return a
    else:
    	return b

def larger_between_two(a,b):
    return max(a,b)


def test_larger_between_two():
	# add two more test cases here
	assert(larger_between_two(4,5) == 5)

# 2. compare three numbers and return the largest.
#    Make use of the larger_between_two function that you've already written.
def largest_among_three(a,b,c):
	bigAB = larger_between_two(a, b)
	return larger_between_two(bigAB, c)

def largest_among_three(a,b,c):
	return max([a, b, c])

# Avoid too long line:
# return larger_between_two(larger_between_two(a, b), larger_between_two(b, c))

def test_largest_among_three():
	# add two more test cases here
	assert(largest_among_three(4,5,3) == 5)

# 3. You are hungry and are deciding what to cook. You only know three recipes, ordered by preference:
#    1. Hamburgers, which requires 2 pounds of ground beef and 2 slices of bread.
#    2. Peanut butter sandwich, which requires 1 ounce of peanut butter and 2 slices of bread.
#    3. Kebabs, which requires 1 pound of ground beef and 3 onions.
# 
# Your job is to make a function that outputs what to cook given the available ingredients.
# It has the following signature:
# whatToCook(beef, peanutButter, bread, onions)
# - `beef` is an integer that gives the number of pounds of beef available
# - `bread` is an integer that gives how many slices of bread are available
# - `peanutButter` is an integer that gives how many ounces of peanut butter are available
# - `onions` is an integer that gives how many onions are available
# The function should return a string, either "Hamburger", "Peanut Butter Sandwich", "Kebab"
# depending on what you want to make (remember, make the things you prefer first!). 
# If none of these are possible, return "You are hungry!"
def whatToCook(beef, peanutButter, bread, onions):
	if beef >= 2 and bread >= 2:
		return "Hamburger"
	elif peanutButter >= 1 and bread >= 2:
		return "Peanut Butter Sandwich"
	elif beef >= 1 and onions >= 3:
		return "Kebab"
	else:
		return "You are hungry!"

def test_whatToCook():
	# add at least two more test cases
	assert(whatToCook(1, 0, 0, 3) == "Kebab")


# 4. Given a list of integers, return the sum all of the even integers in the list.
def sumEven(l):
	if l == []:
		return 0
	else:
		head = l[0]
		tail = l[1:]
		if head % 2 == 0:
			return head + sumEven(tail)
		else:
			return sumEven(tail)

def test_sumEven():
	assert(sumEven([1, 2, 4]) == 6)


# 5. Given a list of integers l, return that list in reverse order
# Hint: Two lists l1 and l2 can be combined using 'l1 + l2'
def reverse(l):
	if l == []:
		return []
	else:
		head = l[0]
		tail = l[1:]
		return reverse(tail) + [head]

def test_reverse():
	assert(reverse([1, 2, 3]) == [3, 2, 1])

# 6. Given a list of integers, return a list that doubles each element if the previous element in the list was even.
# The first element in the list is never doubled.
# Hint: You will need to add an extra function to do this! What is its signature?

def helper(l, prevIsEven):
	if l == []:
		return []
	else:
		head = l[0]
		tail = l[1:]
		curIsEven = head % 2 == 0
		if prevIsEven:
			return [head * 2] + helper(tail, curIsEven)
		else:
			return [head] + helper(tail, curIsEven)



def doubleIfPreviousEven(l):
	return helper(l, False)

def test_doubleIfPreviousEven(l):
	assert(doubleIfPreviousEven([1, 2, 3, 4]) == [1, 2, 6, 4])
	assert(doubleIfPreviousEven([0, 2, 4, 2]) == [0, 4, 8, 4])
