#Program to find intersection of two sorted arrays and arranging them

A1 = [1,2,4,6,7,8,10]
A2 = [2,3,5,6,7,9,10,15]

m = len(A1)
n = len(A2)

def intersectionOfArrays(A1,A2,m,n):
    i, j = 0, 0
    intersection = []
    #traverse arrays
    while i < m and j < n:
        if A1[i] == A2[j]:
            intersection.append(A1[i])
            i += 1
            j += 1
            
        elif A1[i] < A2[j]:
            i += 1

        else:
            j += 1
    
    return intersection

print("Intersection: ", intersectionOfArrays(A1,A2,m,n))