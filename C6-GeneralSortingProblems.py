# Program to rotate an array n times

#input array, length and 'n'
def rotation(A, n, A_size):
    for i in range(n):
        rotate(A, A_size)

#rotate the array tthe left by 1 place
def rotate(A, A_size):
    temp = A[0]
    for i in range(A_size - 1):
        A[i] = A[i + 1]
        A[A_size - 1] = temp

def printArray(A, a_size):
    for i in range (a_size):
        print("%d"% A[i], end=' ')
    print('\n')

A = [ 31, 1, 31, 85, 2, 54, 56, 42, 3]
print(A, len( A))
rotation(A, 3, len(A))
printArray(A, len(A))
