#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 1

import random #used for choosing random pivot

#class for storing pair's details
class Pair:

    #initialises product pair
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.product = a*b

#recursive method for sorting pairs by products
def sortByProduct(objList):

    #base case for when segment's length is 1
    if(len(objList))==1:
        return objList

    smaller=[] #initialized for storing the smaller segment of the list
    equivalent=[] #initialized for storing the element at the pivot
    greater=[] #initialized for storing the greater segment of the list

    #randomly chosen pivot selected from list of pairs
    pivot = objList[random.randint(0,len(objList)-1)]

    #for loop to go through the list of pairs
    for x in objList:

        #when x is less, append to smaller segment
        if(x.product < pivot.product):
            smaller.append(x)

        #when x is at the pivot, store element into equivalent
        elif(x.product==pivot.product):
            equivalent.append(x)

        #when x is greater, append to greater segment
        elif(x.product > pivot.product):
            greater.append(x)

        else:
            print("An unknown error has occurred during sorting by Product")

    #recursively calls method to work on the smaller and greater segment, then returns on backtracking
    return sortByProduct(smaller) + equivalent + sortByProduct(greater)

#method for finding product matches
def findProductMatches(rangeList):

    pairList = [] #initialized for storing products pairs and their components

    # outer loop for a equivalent
    for x in rangeList:

        # inner loop for b equivalent
        for y in rangeList:

            if(y>x): #condition to avoid repeated a*b combinations
                pairList.append(Pair(x,y))

    print(":)")

    for x in pairList:
        print "u:%d"%x.product

    print(":)")

    pairList = sortByProduct(pairList)

    for x in pairList:
        print "s:%d"%x.product

findProductMatches(range(1,1025))

