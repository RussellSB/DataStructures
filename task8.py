#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 8

import math #for pi

#recursive function for finding the factorial of a number x
def _factorial(x):

    #base case, factorial of 0 is 1
    if(x == 0):
        return 1.0

    # calls recursively until base case
    return x * _factorial(x-1)


#function for calculating sin(x) through sum of first t terms
def sin(x,t):

    sum=0.0 #initialised sum

    #if x is out of the range from -2PI to 2PI, x modulo 2PI
    if(x< -(2 * math.pi) or x>(2 * math.pi)):
        x = x%(2*math.pi)

    #for loop for evaluating sin(x) using MacLaurin's Theorem
    for n in range(0,t+1):

        numerator = ((-1)**n) * (x**((2*n)+1))
        denominator = _factorial((2*n)+1)
        sum += numerator/denominator

    return sum #returns answer

#function for calculating cos(x) through sum of first t terms
def cos(x,t):

    sum=0.0 #initialised sum

    # if x is out of the range from -2PI to 2PI, x modulo 2PI
    if (x < -(2 * math.pi) or x > (2 * math.pi)):
        x = x % (2 * math.pi)

    # for loop for evaluating cosx using MacLaurin's Theorem
    for n in range(0,t+1):

        numerator = ((-1)**n)*(x**(2*n))
        denominator = _factorial(2*n)
        sum += numerator/denominator

    return sum #returns answer

a=50.0 #for x in radians
t=90 #for t trials
print("sin(%.4f) with %d trials = %.9f"%(a,t,sin(a,t)))
print("cos(%.4f) with %d trials = %.9f"%(a,t,cos(a,t)))
