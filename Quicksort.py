

def partition(alist, first, last):

    print("New parsing iteration")
    print(alist[first:last+1])

    pivotvalue = alist[first]
    print("pivot", pivotvalue)

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        print("Parse from Left")
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        print ("LeftMark", leftmark, "\n")

        print ("Parse from Right")
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        print ("RightMark", rightmark, "\n")

        if rightmark < leftmark:
            done = True
        else:
            print("switch",alist[leftmark], alist[rightmark] )
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

        print(alist[first:last+1],"\n")

    print("Done Parsing, Move the Pivot")
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    print(alist[first:last+1],"\n")
    return rightmark


def quick_sort(array, start, end):
    comparisons = 0
    if start >= end:
        return comparisons

    p = partition(array, start, end)
    comparisons += (end-start)
    comparisons +=quick_sort(array, start, p-1)
    comparisons +=quick_sort(array, p+1, end)
    return comparisons

#array = [54,26,93,17,77,31,44,55,20]

array = [26, 54, 65]
print(array, "\n")
comparisons = quick_sort(array, 0, len(array) - 1)
print(array)
print("# Comparisons ", comparisons)