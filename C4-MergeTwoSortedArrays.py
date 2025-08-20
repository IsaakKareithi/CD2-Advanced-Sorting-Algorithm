#Program to merge two sorted arrrays

#Merge A1 and A2 into A3
def mergeTwoArrays(A1,A2,m,n):
    # Size of A3 
    A3 = [None] * (m + n)
    i=0
    j=0
    k=0

    #traversing both arrays
    while i < m and j < n:

        #Comparing current elements of A1 and A2
        if A1[i] < A2[j]:
            A3[k] = A1[i]
            k = k +1
            i = i + 1
        
        else:
            A3[k] = A2[j]
            k = k + 1
            j = j + 1

    #Remaining items of first array
    while i < m:
        A3[k] = A1[i]
        k = k + 1
        i = i + 1
    
    #remaining items of 2nd array
    while j < n:
        A3[k] = A2[j]
        k = k + 1
        j = j + 1
    print("Merged Arrays: ")
    for i in range(m + n):
        print(str(A3[i]), end =' ')

#driver code 
#m is size of A1 and n is size of A2
A1 = [2,4,6,8]
m = len(A1)

A2 = [10,12,14,16]
n = len(A2)

mergeTwoArrays(A1,A2,m,n)
