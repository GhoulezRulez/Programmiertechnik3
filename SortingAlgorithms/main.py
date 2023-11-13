

#Implement sorting algorithms

## functions

#bubblesort
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

#insertionsort
def insertionsort(array):
    pass
#mergesort
def mergesort(array):
    
    

##main

array1 = [4,2,67,3,74,7,32,3,7,6,0,1]

print(array1[2])
print(len(array1))


print(bubblesort(array1))
print(mergesort(array1))
