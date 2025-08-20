#Program of merge sort in python 
def mergeSorting(A):
    if len(A)> 1:
        mid  =len(A) // 2
        left = A[:mid]
        right = A[mid:]

        #Recursive call on each half
        mergeSorting(left)
        mergeSorting(right)

        #Two iterations for traversing two halves
        i = 0
        j = 0

        #Iterator for the main array
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                
                #The value from the left half has been used
                A[k] = left[i]
                i += 1

            else:
                A[k] = right[j]
                j += 1

            #move to the next slot
            k += 1
    
        # For all the remaining values
        while i <len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

A = [59,80,32,17,90,31,56,55,21]
print("Unsorted array : {}".format(A))
mergeSorting(A)
print("Sorted array: {}".format(A))