# Program to sort 0s and 1s in an array
def sortZeroOne(A,n):

    #Count the number of 0s in an array
    count = 0

    for i in range(0,n):
        if (A[i] == 0):
            count = count + 1

    #Filling the A with 0 till count
    for i in range (0, count):
        A[i] = 0

    #Filling the remainging space with 1 
    for i in range (count, n):
        A[i] = 1

#Driver code 
A = [0,1,0,1,1,0,1,1,1,0]
n = len(A)

sortZeroOne(A, n)
print("Sorted array is: ", end=' ')
for i in range(0 ,n):
    print(A[i], end=' ')