#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 2

import operator #for operator functionality

#defines operator characters and corresponding functions
ops = { '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.div
}

#class used to implement ADT Stack
class Stack:

    #initializes stack
    def __init__(self):
        self.items = []

    #pushes to the top of the stack
    def push(self, item):
        self.items.append(item)

    #pops top element of the stack
    def pop(self):
        return self.items.pop()

    #gets size of the stack
    def size(self):
        return len(self.items)

    #used for printing the stack
    def __str__(self):
        return str(self.items)

#method used for RPN Calculator
def rpnCalc(String):

    s = Stack() #instance of Stack
    temp = "" #initializes String to temporarily store numbers
    num = 0 #initializes number to store current number

    #scanning each token in the string and evaluating with stack
    for x in String:

        #when token is a number or decimal point
        if x in ['0','1','2','3','5','6','7','8','9','.']:
           temp+=x #concatenate to temp

        #when token is a space
        elif x==" ":

            #if the previous argument was a number, push to stack
            if temp!="":
                num = float(temp)  #convert to float
                s.push(num)  #push into stack
                temp = ""  #clear temp
                print s #print stack

            #note that if operator was before, nothing is performed

        #when token is an operator
        elif x in ops:

            #when stack has less than two elements
            if s.size()<2:
                print("Error: At least two parameters required before the operator. -1 returned")
                return -1

            b = s.pop()
            a = s.pop()
            op = ops[x]

            s.push(op(a,b))

            print s #print stack

        else:
            print("Error: Invalid character \' %s \' detected. -1 returned"%x)
            return -1

    return s.pop() #returns calculated number after stack evaluation

expression = "3 5 x 7 9 / 3 8 + x + 9 +"
print("Evaluating \"%s\" using RPN: "%(expression))
print("Answer = %.1f"%rpnCalc(expression))



