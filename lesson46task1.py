def bidirectional_bubble_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Пряма перевірка
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        right -= 1

        # Обернена перевірка
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = bidirectional_bubble_sort(arr)
print("Sorted array:", sorted_arr)