# Program to Unite two sorted arrays

def unionOfArrays(A1, A2, m, n):
    i, j = 0, 0
    
    while i < m and j < n:
        if A1[i] < A2[j]:
            print(A1[i], end=' ')
            
            i += 1

        elif A2[j] < A1[i]:
            print(A2[j], end=' ')
            j += 1

        else: 
            print(A2[j], end =' ')
            j += 1
            i += 1

    # Remaining elments of the greater sized array
    while i < m: 
        print(A1, end = ' ')
        i += 1

    while j < n: 
        print(A2[j], end=' ')

#Driver code
A1 = [1,2,6,8,7,9]
A2 = [2,3,4,5,6,7]

m = len(A1)
n = len(A2)
unionOfArrays(A1, A2, m, n)