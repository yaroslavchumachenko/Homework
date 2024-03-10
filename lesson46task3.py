def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, partition_limit):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left, partition_limit) + middle + quicksort(right, partition_limit)
    return arr

import random
import time

random.seed(10)

list_sizes = [100, 500, 1000, 5000, 10000]
partition_limits = [5, 10, 20, 50]

for size in list_sizes:
    for limit in partition_limits:
        unsorted_list = [random.randint(1, 1000) for _ in range(size)]

        start_time = time.time()
        sorted_list = quicksort(unsorted_list.copy(), partition_limit=limit)
        end_time = time.time()

        elapsed_time = end_time - start_time

        print(f"List size: {size}, Partition Limit: {limit}, Elapsed Time: {elapsed_time:.6f} seconds")
