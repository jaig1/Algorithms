def partition(alist, first, last):

    print("New parsing iteration")
    print(alist[first:last+1])

    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        print("Parse from Left")
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        print ("LeftMark", leftmark, alist[leftmark], "\n")

        print ("Parse from Right")
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        print ("RightMark", rightmark, alist[rightmark])

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
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [54,26,93,17,77,31,44,55,20]
print(array, "\n")
quick_sort(array, 0, len(array) - 1)
print(array)