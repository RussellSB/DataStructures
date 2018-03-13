#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 8

import math #package for math.factorial

#function for calculating sinx through sum of first n terms
def sin(x,n):

    sum=0.0 #initialised sum

    #for loop for evaluating sinx derived from Taylor's Theorem
    for k in range(0,n):
        numerator = ((-1)**k) * (x**((2*k)+1))
        denominator = math.factorial((2*k)+1)
        sum += float(numerator/denominator)

    return sum #returns answer

def cos(x,n):

    sum=0.0 #initialised sum

    # for loop for evaluating cosx derived from Taylor's Theorem
    for k in range(0,n):
        numerator = ((-1)**k)*(x**(2*k))
        denominator = math.factorial(2*k)
        sum += float(numerator/denominator)

    return sum #returns answer

a=2.0 #for x in radians
n=85 #for n trials
print("sin(%.4f) with %d trials = %.9f"%(a,n,sin(a,n)))
print("cos(%.4f) with %d trials = %.9f"%(a,n,cos(a,n)))




