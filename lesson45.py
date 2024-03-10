# Бінарний пошук

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

# Приклад використання:
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search_recursive(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Елемент {x} знаходиться на позиції: {result}")
else:
    print("Елемент відсутній у масиві")


# Пошук Фібоначі 
    
def fibonacci_search(arr, x, n):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2
    
    while (fib < n):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2
    
    offset = -1
    
    while (fib > 1):
        i = min(offset + fib_m_minus_2, n - 1)
        
        if (arr[i] < x):
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i
        
        elif (arr[i] > x):
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
        
        else:
            return i
    
    if(fib_m_minus_1 and arr[offset+1] == x):
        return offset+1
    
    return -1

# Приклад використання:
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85
n = len(arr)

result = fibonacci_search(arr, x, n)
if result != -1:
    print(f"Елемент {x} знаходиться на позиції: {result}")
else:
    print("Елемент відсутній у масиві")

