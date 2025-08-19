A = []
n = len(A)

interval= n // 2

while interval > 0 :
    for i in range(interval, n):
        temp = A[i]
        j = i
        while j >= interval and A[j - interval] > temp:
            A[j] = A[j-interval]
            j-=interval

        A[j] = temp
    interval //= 2       

size = int(input("Enter the size of the array: "))

print('Enter the elements of the array: ')
for i in range(size):
    num = int(input(f"Element {i+1}: "))
    A.append(num)

print("original array: ",A)

print(A)