
import random

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = sorted ([arr[0], arr[len(arr)//2], arr[-1]])[1]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

lista1 = random.sample(range(1,1000000), 1000)
lista2 = random.sample(range(1,1000000), 1000)
lista3 = random.sample(range(1,1000000), 1000)
lista4 = random.sample(range(1,1000000), 1000)

lista1 = quicksort(lista1)
lista2 = quicksort(lista2)
lista3 = quicksort(lista3)
lista4 = quicksort(lista4)

print("Lista ordenada 1: ", lista1)
print("Lista ordenada 2: ", lista2)
print("Lista ordenada 3: ", lista3)
print("Lista ordenada 4: ", lista4)
