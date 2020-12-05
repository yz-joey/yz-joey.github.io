from functools import reduce


#1. Write a function to count the number of integers in l that 
# contains a digit 7.
# Hint: an integer i can be converted to a string with str(i).
# Example: count_7([1,17,72,77]) returns 3. 

def count_7(l):
    count = 0
    for num in l:
        if "7" in str(num):
            count += 1
    return count

def count_7_nest(l):
    count = 0
    for num in l:
        while num != 0:
            if num % 10 == 7:
                count += 1
                num = 0
            num = num % 10
    return count

        
#2. Write a function to calculate the sum of following series where n is given
#   as the input to the function  1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n

def series(n):
    result = 0
    for i in range(1,n+1):
        result += 1/i
    return result


#3. Write a function to create the multiplication table (from 1 to 10)
#   of a number n and returns a list. 
#   Input: 6
#   Expected Output: [6,12,18,24,30,36,42,48,54,60]

def multTable(n):
    result = []
    for i in range(1, 11):
        result += [i*n]  # result.append(i*n)
    return result


#4. Write a function isPrime to identify if a given number is prime 
# (A prime number (or a prime) is a natural number greater than 1 
# that is not a product of two smaller natural numbers.)
#   input: 11
#   output: True

def isPrime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime



#5. Write a function getPrimes to return a list of primes between 2 and n.
#   Please use isPrime defined above.
#   Input : 10
#   output : [2,3,5,7]

def getPrimes(n):
    result = []
    for i in range(2, n+1):
        if isPrime(i):
            result += [i] # result.append(i)
    return result

#6. Write a function draw to print a triangle pattern with a pre-defined 
# number of rows.
# Example: draw(5) will print the following pattern. 
# Hint: use print(). return is not needed in this function. 

#
##
###
####
#####

def draw(n):
    for i in range(1, n+1):
        acc = ""
        for j in range(i):
            acc += "#"
        print(acc)

def draw_2(n):
    for i in range(1, n+1):
        acc = "#" * i
        print(acc)



#7. Consider the dictionary: rational = {"num": a, "denom": b}, where a and b are integers. b != 0
#   (1). Given a list of rationals write a function to return the maximum value
#   Input : [{"num": 1, "denom": 2}, {"num": 1, "denom": 4}]
#   Output: {"num": 1, "denom": 2}
#   (2)*. Given a list of rationals, write a function to return the sum of their reciprocal.
#   Let rational be a/b, its reciprocal is defined as b/a. 
#   a/b + c/d = (a*d + b*c) / (b*d)
#   The results will not necessarily be in lowest terms.
#   Hint: You can start with sum = {"num": 0, "denom": 1}
#   Input : [{"num": 1, "denom": 2}, {"num": 1, "denom": 4}]

#7 (1):
def maxRationals(rationals):
    maxRational = rationals[0]
    i = 1
    while i < len(rationals):
        if rationals[i]["num"] / rationals[i]["denom"] > maxRational["num"] / maxRational["denom"]:
            maxRational = rationals[i]
        i += 1
    return maxRational


#7 (2)*:
def r_add(r1, r2):
    num = r1["num"] * r2["denom"] + r1["denom"] * r2["num"]
    denom = r1["denom"] * r2["denom"]
    return {"num": num, "denom": denom}

def sumOfReciprocal(rationals):
    accum = {"num": 0, "denom": 1}
    for r in rationals:
        reciprocal = {"num": r["denom"], "denom": r["num"]}
        accum = r_add(accum, reciprocal)
    return accum


# 8*. Implement question 6 using (i) recursion and (ii) reduce operator. 
#7(1)  using recursion
def maxRationals_rec(rationals):
    if len(rationals) == 1:
        return rationals[0]
    else:
        head = rationals[0]
        tail = rationals[1:]
        tailRes = maxRationals_rec(tail)
        if head["num"]/head["denom"] > tailRes["num"]/tailRes["denom"]:
            return head
        else:
            return tailRes

#7(1) using reduce
def maxRationals_reduce(rationals):
    return reduce(lambda x,y: x if x["num"]/x["denom"] > y["num"]/y["denom"] else y, rationals) 


#7(2) using recursion:
def sumOfReciprocal_rec(rationals):
    if rationals == []:
        return {"num": 0, "denom": 1}
    else:
        head = rationals[0]
        reciprocal = {"num": head["denom"], "denom": head["num"]} 
        tail = rationals[1:]
        tailRes = sumOfReciprocal_rec(tail)
        return r_add(reciprocal, tailRes)
        
#7(2) using reduce
def sumOfReciprocal_reduce(rationals):
    reciprocals = list(map(lambda x: {"num": x["denom"], "denom": x["num"]}, rationals))
    return reduce(r_add, reciprocals)
