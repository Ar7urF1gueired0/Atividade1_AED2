import random

def selectionsort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    
lista1 = [i for i in range(1000, 0, -1)]
lista2 = [i for i in range(10000, 0, -1)]
lista3 = [i for i in range(2000, 0, -2)]
lista4 = [i for i in range(20000, 0, -2)]

selectionsort(lista1)
selectionsort(lista2)
selectionsort(lista3)
selectionsort(lista4)

print("Lista ordenada 1: ", lista1)
print("Lista ordenada 2: ", lista2)
print("Lista ordenada 3: ", lista3)
print("Lista ordenada 4: ", lista4)