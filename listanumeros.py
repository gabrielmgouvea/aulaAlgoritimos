import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i):
            if lista[j] > lista[j+1]:
             (lista[j], lista[j+1]) = (lista[j+1], lista[j])

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

n = 10000
random_list_bubble = [random.randint(0, 100) for i in range(n)]
random_list_selection = random_list_bubble.copy()

start_time = time.time()
bubble_sort(random_list_bubble)
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(random_list_selection)
selection_sort_time = time.time() - start_time

print(f"Bubble Sort demorou: {bubble_sort_time:.4f} segundos para {n} elementos.")
print(f"Selection Sort demorou: {selection_sort_time:.4f} segundos para {n} elementos.")
