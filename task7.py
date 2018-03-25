#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 7

#recursive method to finding the max number of the list
def _findMax(list):

    length = len(list) #getting current length of list

    #base case to check if list is 1 in length
    if length==1:
        return list[0]

    #compares last two elements
    if list[length - 1] > list[length - 2]:
        del list[length - 2] #delete element before the last, shift last to the left
    else:
        del list[length - 1] #delete element at the last position

    return _findMax(list) #calls method recursively

list = range(1,1000)
print("The max number in %s is:"%(str(list)))
print(_findMax(list))