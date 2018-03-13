#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 5

#finding the root using Newton-Rhapson method
def NewtonRhapson(n):

    x = 0 #setting initial x as 0
    x1 = n #initializing x1 as n

    #compares current approximation to previous for 9 decimal places
    while(round(x1,9)!=round(x,9)):

        x = x1 #sets current x to previous x1, for function calculation

        function = x**2 - n #f(x) of n
        function_deriv = 2*x #f'(x) of n

        x1 = x - (function/function_deriv) #Newton-Rhapson formula for finding the root

    return round(x,9) #returns answer accurate to 9 d.p.


n=123456789.0
print("Using the Newton-Rhapson Method, the square root of %f is %.9f"%(n,NewtonRhapson(n)))
