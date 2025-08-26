#Program to check if array is rotated and sorted

#Input array and constants
arr = [3, 4, 5, 1, 2]
n = len(arr)
count = 0 

#iterating loop from 1 to length of array
for i in range(1, n):

    #Comparing items of array
    if(arr[i-1] > arr[i]):
        count += 1

#in case of special cases when comparing,
#Last element to the first is compared

if(arr[n - 1] > arr[0]):
    count += 1 

#Driver code
print(count <= 1)