########### BISECTION SEARCH ###########
##x = 100
##y = 0
##high = x
##low = y
##guess = int((high + low)/ 2)
##
##print('Please think of a number between ',y,'and ',x,'!')
##print('Is your secret number', guess, '?')
##answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
##while answer != 'c':
##    if answer == 'h':
##        high = guess
##        guess = int((high + low)/ 2)
##        print('Is your secret number', guess, '?')
##        answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
##    elif answer == 'l':
##        low = guess
##        guess = int((high + low)/ 2)
##        print('Is your secret number', guess, '?')
##        answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
##    else:
##        print('Sorry, I did not understand your input.')
##        print('Is your secret number', guess, '?')
##        answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
##print('Game over. Your secret number was: ', guess)


########### BINARY REPRESANTATION ###########
#### Integers #####
##num = 11
##
##if num < 0:
##    isNeg = True
##    num = abs(num)
##else:
##    isNeg = False
##result = ''
##if num == 0:
##    result = '0'
##while num > 0:
##    result = str(num%2) + result
##    num = num//2
##if isNeg:
##    result = '-' + result
##print(result)

#### Floats #####
##import ctypes
##def binRep(num):
##    binNum = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value)[2:]
##    print("bits: " + binNum.rjust(32,"0"))
##    mantissa = "1" + binNum[-23:]
##    print("sig (bin): " + mantissa.rjust(24))
##    mantInt = int(mantissa,2)/2**23
##    print("sig (float): " + str(mantInt))
##    base = int(binNum[-31:-23],2)-127
##    print("base:" + str(base))
##    sign = 1-2*("1"==binNum[-32:-31].rjust(1,"0"))
##    print("sign:" + str(sign))
##    print("recreate:" + str(sign*mantInt*(2**base)))
##
##binRep(0.1)


########### FUNCTIONS ###########
##def square(x):
##    '''
##    x: int or float.
##    '''
##    result = x * x
##    return result


##def evalQuadratic(a, b, c, x):
##    '''
##    a, b, c: numerical values for the coefficients of a quadratic equation
##    x: numerical value at which to evaluate the quadratic.
##    '''
##    result = a * (x*x) + b * x + c
##    return result

# def square(x):
#     y = x * x
#     return y

#
# def fourthPower(x):
#     '''
#     x: int or float.
#     '''
#     y = square(square(x))
#     return y

# def odd(x):
#     '''
#     x: int
#
#     returns: True if x is odd, False otherwise
#     '''
#     y = (x % 2 != 0)
#     return y

########## RECURSION  ###########
# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     result = 1
#     while exp > 0:
#         result *= base
#         exp -= 1
#     return result

# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     if exp == 1:
#         return base * exp
#     elif exp == 0:
#         return 1
#     else:
#         return base * recurPower(base, exp -1)


# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     if a == b:
#         result = a
#         return result
#     elif a < b:
#         result = a
#         while b % result != 0:
#             result-= 1
#             while a % result != 0:
#                 result-=1
#         return result
#     else:
#         result = b
#         while a % result != 0:
#             result-= 1
#             while b % result != 0:
#                 result-=1
#         return result

# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     if b == 0:
#         return a
#     else:
#         return gcdRecur(b,a%b)

# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     if int(len(aStr)) <= 0:
#         return False
#     elif int(len(aStr)) == 1:
#         return char == aStr
#     elif char == aStr[int(len(aStr)/2)]:
#         return True
#     elif char < aStr[int(len(aStr)/2)]:
#         return isIn(char,aStr[:int(len(aStr)/2)])
#     else:
#         return isIn(char,aStr[int(len(aStr)/2):])

# #math library dependency has to be imported first
# import math

# A regular polygon has 'n' number of sides. Each side has length 's'.
# * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
# * The perimeter of a polygon is: length of the boundary of the polygon

######### PROBLEM 1 ############

# def polysum(n, s):
#     '''
#     #     n: (int or float) number of sides of a polygon
#     #     s: (int or float )length of each side
#     #
#     #     returns: the sum of the area and square of the perimeter of the regular polygon
#     #     '''
#     polygonarea = (0.25*n*(s*s))/(math.tan(math.pi/n))
#     polygonperimeter = s*n
#     return round(polygonarea + (polygonperimeter * polygonperimeter),4)

######### PROBLEM SET 2 ############

# def remainingdebt(balance, annualInterestRate, monthlyPaymentRate):
#     for i in range(12):
#         unpaidbalance = balance - (balance * monthlyPaymentRate)
#         unpaidbalance = unpaidbalance + (unpaidbalance * (annualInterestRate/12))
#         balance = unpaidbalance
#         i += 1
#     print("Remaining balance:",round(balance,2))

######### PROBLEM SET 2 - paying off debt in a year ############

# def unpaidbalance(balance, annualInterestRate, monthlyFixedPayment):
#         for i in range(12):
#             unpaidbalance = balance - monthlyFixedPayment
#             unpaidbalance = unpaidbalance + (unpaidbalance * (annualInterestRate/12))
#             balance = unpaidbalance
#             i += 1
#         return balance
#
# #def mfp(balance, annualInterestRate):
# monthlyFixedPayment = 0
# while unpaidbalance(balance, annualInterestRate, monthlyFixedPayment) > 0:
#     unpaidbalance(balance, annualInterestRate, monthlyFixedPayment)
#     monthlyFixedPayment += 10
# print("Lowest Payment:",monthlyFixedPayment)

######### PROBLEM 3 - BISECTION SEARCH ############

# def unpaidbalance(balance, annualInterestRate, monthlyFixedPayment):
#         for i in range(12):
#             unpaidbalance = balance - monthlyFixedPayment
#             unpaidbalance = unpaidbalance + (unpaidbalance * (annualInterestRate/12))
#             balance = unpaidbalance
#         return balance
#
# def mfpbisectionsearch(mfplow, mfphigh, balance, annualInterestRate):
#         guess = (mfplow + mfphigh) / 2
#         unpaid = unpaidbalance(balance, annualInterestRate, guess)
#
#         if unpaid > 0.01:
#             return mfpbisectionsearch(guess, mfphigh, balance, annualInterestRate)
#         elif unpaid < -0.01:
#             return mfpbisectionsearch(mfplow, guess, balance, annualInterestRate)
#         else:
#             return guess
#
# def mfp(balance, annualInterestRate):
#     mfplow = balance / 12
#     mfphigh = (balance * (1+(annualInterestRate/12.0))**12)/12
#
#     monthlyFixedPayment = mfpbisectionsearch(mfplow, mfphigh, balance, annualInterestRate)
#
#     print("Lowest Payment:", round(monthlyFixedPayment,2))
#
# mfp(999999, 0.18)
