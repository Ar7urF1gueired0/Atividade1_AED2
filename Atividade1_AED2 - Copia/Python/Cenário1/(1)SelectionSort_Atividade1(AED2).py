import random

def selectionsort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    
lista1 = random.sample(range(1,1000000), 1000)
lista2 = random.sample(range(1,1000000), 1000)
lista3 = random.sample(range(1,1000000), 1000)
lista4 = random.sample(range(1,1000000), 1000)

selectionsort(lista1)
selectionsort(lista2)
selectionsort(lista3)
selectionsort(lista4)

print("Lista ordenada 1: ", lista1)
print("Lista ordenada 2: ", lista2)
print("Lista ordenada 3: ", lista3)
print("Lista ordenada 4: ", lista4)