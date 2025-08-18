#program to find intersection of two sorted arrays

#Initializing the two arrays
A1 = [1,2,4,5,6,8,10]
A2 = [2,3,5,7,10,15]

#Initializing m and n 
m = len(A1)
n = len(A2)

i, j = 0, 0
while i < m and j < n:
    #Comparing array items
    if A1[i] < A2[j]:
        i += 1
    elif A2[j] < A1[i]:
        j += 1
    else:
        #Printing intersection of two arrays
        print(A2[j],end=' ')
        j += 1 
        i += 1