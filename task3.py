#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 3

import time #used for execution time comparison

#checks if number is prime
def isPrime(n):

    '''
    The range for the loop is set from 2 to n, as we are concerned with finding factors
    that aren't 1 and n itself. If no factors that aren't 1 and n are found then by definition
    it is a prime number.
    '''

    #if 2 then prime number
    if(n==2):
        return True
    else:
    #if n is not 2 then test if n has a factor between 2-n
        for x in range(2,n):

            r = n%x #calculating remainder for current test

            if(r==0): #if a factor is found, n is not prime
                return False

        # if a factor isn't found in the loop, n is prime
        return True

#finds all prime numbers less than or equal to n using isPrime()
def findPrimes1(n):

    start_time=time.time() #starts timer

    primes = [] #initialized to later store prime numbers

    #for loop from range 2-n (including n)
    for x in range(2,n+1):

        # appends prime numbers to list "primes" when isPrime(x) is True
        if(isPrime(x)==True):
            primes.append(x)

    end_time = time.time() #ends timer

    print("Total time: %0.5f"%(end_time-start_time)) #prints executuion time
    return primes



#finds all prime numbers less than or equal to n using Sieve of Eratosthenes Algorithm
def findPrimes2(n):

    start_time = time.time() #starts timer

    primes = [] #initializes list of prime numbers as empty

    #initializes Boolean list from 2-n (including n)
    sieve = [True for _ in range(n+1)]

    #starts by setting 0 and 1 to False as they are not prime numbers
    sieve[0:1] = [False, False]

    #for loop from 2-n
    for p in range(2, n + 1):

        #if True, access nested loop
        if sieve[p]:

            #set multiples of p to false, starting from 2*p and incrementing by p each iteration
            for i in range(2 * p, n + 1, p):
                sieve[i] = False

    #for loop from 2-n
    for i in range(2, n + 1):

        #if True, after the procedure above, then prime, so add to primes list
        if sieve[i]:
            primes.append(i)

    end_time = time.time() #ends timer

    print("Total time: %0.5f" % (end_time - start_time)) #prints executuion time
    return primes

n1=101
print("Is %d a prime number?: %s"%(n1,isPrime(n1)))

print("------------------------------------")

n2=10000

primes1 = findPrimes1(n2)
print("List of prime numbers up to %d using isPrime() are: "%n2)
print primes1

print("------------------------------------")

primes2 = findPrimes2(n2)
print("List of prime numbers up to %d using Sieve of Eratosthenes are: "%n2)
print primes2

