#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 6

#method solving problem using 2 arrays
def findRepitition(array):

    unique = [] #for storing unique elements
    duplicate = [] #for storing repeated elements

    #when empty array
    unique.append(array[0])

    #loop to scan through array
    for x in array:

        #when unique has contents
        if x in unique and not x in duplicate: #if match found, add to duplicate provided duplicate is not already detected
            duplicate.append(x)
        if x not in unique: #if no match is found, add to unique
            unique.append(x)

    #returns repeated numbers
    return duplicate


array=range(1,1000)+range(1,1000)
duplicates = findRepitition(array)
print("Duplicate numbers in the array %s are: "%str(array))
print duplicates