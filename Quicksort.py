import math
import statistics

class Counter:
    '''
    A simple counter class.
    Useful for counting up the number of
    comparisons made by quicksort.
    '''
    def __init__(self, n=0):
        self.total = n

    def __call__(self, x=0):
        self.total += x

def median ( alist, first, last ):

    firstValue= alist[first]
    lastValue = alist[last]
    middle =  first + math.ceil(last-first)/2
    middleValue = alist[int(middle)]
    list = [firstValue, middleValue, lastValue]
    medianValue = statistics.median(list)
    return alist.index(medianValue)


def partition(alist, first, last, count):

   # print("New parsing iteration")
   # print(alist[first:last+1])


    medianIndex = median(alist, first, last)
    temp = alist[first]
    alist[first] = alist[medianIndex]
    alist[medianIndex] = temp
    #print(alist[first:last + 1])

    pivotvalue = alist[first]
    #print("pivot", pivotvalue)

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        #print("Parse from Left")
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            count(1)


        #print ("LeftMark", leftmark, "\n")

        #print ("Parse from Right")
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
            count(1)


        #print ("RightMark", rightmark, "\n")

        if rightmark < leftmark:
            done = True
        else:
            #print("switch",alist[leftmark], alist[rightmark] )
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

        #print(alist[first:last+1],"\n")

    #print("Done Parsing, Move the Pivot")
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    #print(alist[first:last+1],"\n")
    return rightmark


def quick_sort(array, start, end, count):

    if start >= end:
        return

    p = partition(array, start, end, count)
    quick_sort(array, start, p-1, count)
    quick_sort(array, p+1, end, count)
    return

#array = [54,26,93,17,77,31,44,55,20]
#print(array, "\n")
array = [int(x.rstrip()) for x in open('C:/Users/Jaiganesh/quicksort.txt')]
count= Counter()
comparisons = quick_sort(array, 0, len(array) - 1, count)
print(array)
print("# Comparisons ", count.total)



"""
array = [20, 26, 44, 17, 31]
print(array, "\n")
medianIndex = median(array, 0, len(array) - 1)
print("MedianIndex", medianIndex)
"""