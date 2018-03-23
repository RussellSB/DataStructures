#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 9

def calcSumFib(n):

    prev=0 #initialised to 0
    x=1 #set to 1
    sum=0 #initialised to 0
    temp = 0  # initialised to 0, temporarily stores next number

    for i in range(0,n): #loops for n times

        print(x) #prints current number in the sequence

        #print(x)
        sum+=x

        #incrementing to next elements
        temp = prev + x
        prev = x
        x = temp

    return sum

n=20
print("Sum of the first %d elements in the Fibonacci sequence is %d"%(n,calcSumFib(n)))