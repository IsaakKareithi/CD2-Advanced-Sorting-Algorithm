#program to reverse the same array
A= [1,2,3,4,5,6]

#Initializing start and end 
start = 0
end = len(A)-1

# Reverse A from start to end
while start < end:
    #Swapping the elments of an array to reverse in same array
    A[start], A[end] = A[end], A[start]

    start += 1
    end -= 1

#Driver code 
print('Reversed array is: ')
print(A)