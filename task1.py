#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 1

#method for sorting list of objects by product, calls recursive quickSort
def quickSort(objList, sortBy):

    return _quickSort(objList, 0, objList.length - 1)

def _quickSort(objList, low, high):

    if low < high:



#class for storing pair's details
class Pair:

    #initialises product pair
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.product = a*b

#method for finding product matches
def findProductMatches(rangeList):

    pairList = [] #initialized for storing products pairs and their components

    # outer loop for a equivalent
    for x in rangeList:

        # inner loop for b equivalent
        for y in rangeList:

            #if statement to make sure x and y are distinct
            if(x!=y):
                pairList.append(Pair(x,y))

findProductMatches(range(1,10))

