# Python program for implementation of CountInversions in a given array

def mergeSort(arr):
    inv_count = 0
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        inv_count += mergeSort(L)  # Sorting the first half
        inv_count += mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                inv_count += 1
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return inv_count

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [20, 1, 6, 4, 5]
    print("Given array is", end="\n")
    printList(arr)
    result=mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    print("Number of inversions are", result)
