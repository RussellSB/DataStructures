#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 6

import random #used for choosing random pivot
import time #used for execution time comparison

#recursive quick-sort for findRepetitions2(array)
def quickSort(numList):

    #base case for when segment's length is less than or equal to one
    if(len(numList)<=1):
        return numList

    smaller=[] #initialized for storing the smaller segment of the list
    equivalent=[] #initialized for storing the element at the pivot
    greater=[] #initialized for storing the greater segment of the list

    #randomly chosen pivot selected from list of pairs
    pivot = numList[random.randint(0,len(numList)-1)]

    #for loop to go through the list of pairs
    for x in numList:

        #when x is less, append to smaller segment
        if(x < pivot):
            smaller.append(x)

        #when x is at the pivot, store element into equivalent
        elif(x == pivot):
            equivalent.append(x)

        #when x is greater, append to greater segment
        elif(x > pivot):
            greater.append(x)

        else:
            print("An unknown error has occurred during sorting by number")

    #recursively calls method to work on the smaller and greater segment, then returns on backtracking
    return quickSort(smaller) + equivalent + quickSort(greater)


#method solving problem using 2 arrays
def findRepetition1(array):

    start_time = time.time()  # gets time at start

    unique = [] #for storing unique elements
    duplicate = [] #for storing repeated elements

    #append first element as unique
    unique.append(array[0])

    #loop to scan through array
    for x in array:

        #when unique has contents
        if x in unique and not x in duplicate: #if match found, add to duplicate provided duplicate is not already detected
            duplicate.append(x)
        if x not in unique: #if no match is found, add to unique
            unique.append(x)

    end_time = time.time()  # gets time at end
    print("Total time: %0.5fs" % (end_time - start_time))  # prints execution time

    #returns repeated numbers
    return duplicate


#method solving problem using an implementation of quick-sort
def findRepetition2(array):

    start_time = time.time()  # gets time at start

    array = quickSort(array)
    duplicate = []

    i = 0  # initialized index to 0

    # goes through every index in the array array
    while (i < len(array)):

        # Accesses this during the last iteration when the last index has no matching numbers. Avoids OutOfIndex exception, iterates to exit loop
        if (i == len(array) - 1):
            i += 1

        # If number at index doesnt match next, iterate
        elif (array[i] != array[i + 1]):
            i += 1

        # If current number is seen to match next, access while loop
        elif (array[i] == array[i + 1]):

            duplicate.append(array[i]) #append as duplicate

            # traverses through repeated numbers, iterating over to prepare to scan the next number
            while (i != len(array)-1 and array[i] == array[i + 1]):
                i += 1

        # else statement used for unconsidered scenarios
        else:
            print("Error: something wrong has occurred during traversing.")

    end_time = time.time()  # gets time at end
    print("Total time: %0.5fs" % (end_time - start_time))  # prints execution time

    #returns repeated numbers
    return duplicate


array=range(1,10000)+range(1,10000)

repetitions1 = findRepetition1(array)
print("Using the 2-array unique comparison method;")
print("Duplicate numbers in the array %s are: \n%s\n"%(array,repetitions1))

repetitions2 = findRepetition2(array)
print("Using the Quick-sort implementation method;")
print("Duplicate numbers in the array %s are: \n%s\n"%(array,repetitions2))