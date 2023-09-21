import random

def countingsort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num]+=1 

    for i in range(1, max_value+1):
        count[i] += count[i-1]

    output = [0] * len(arr)

    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1

    return output

lista1 = random.sample(range(1,1000000), 1000)
lista2 = random.sample(range(1,1000000), 1000)
lista3 = random.sample(range(1,1000000), 1000)
lista4 = random.sample(range(1,1000000), 1000)

lista1 = countingsort(lista1)
lista2 = countingsort(lista2)
lista3 = countingsort(lista3)
lista4 = countingsort(lista4)

print("Lista Ordenada 1: ", lista1)
print("Lista Ordenada 2: ", lista2)
print("Lista Ordenada 3: ", lista3)
print("Lista Ordenada 4: ", lista4)