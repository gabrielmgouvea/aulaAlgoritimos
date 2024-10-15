import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

n = 10000
random_list_bubble = [random.randint(0, 1000000) for _ in range(n)]
random_list_selection = random_list_bubble.copy()

start_time = time.time()
bubble_sort(random_list_bubble)
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(random_list_selection)
selection_sort_time = time.time() - start_time

print(f"Bubble Sort demorou: {bubble_sort_time:.4f} segundos para {n} elementos.")
print(f"Selection Sort demorou: {selection_sort_time:.4f} segundos para {n} elementos.")
