#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 7

def _findMax(list):

    length = len(list) #getting current length of list

    #checks if list is 1 in length
    if length==1:
        return list[0]

    #compares last two elements
    if list[length - 1] > list[length - 2]:
        del list[length - 2] #delete element before the last, shift last to the left
    else:
        del list[length - 1] #delete element at the last position

    return _findMax(list) #calls method recursively

list = [1,2,3,4,5,60,6,7,80,9,10]
print("The max number in %s is %d"%(str(list),_findMax(list)))