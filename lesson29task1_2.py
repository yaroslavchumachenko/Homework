import multiprocessing
import time

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def squares(n):
    return [i**2 for i in range(1, n + 1)]

def cubes(n):
    return [i**3 for i in range(1, n + 1)]

def main():
    start_time = time.time()
    pool = multiprocessing.Pool(processes=4)
    results = pool.map_async(fibonacci, [10000], chunksize=1).get()
    factorial_result = factorial(100000)
    squares_result = squares(10000)
    cubes_result = cubes(100000)
    pool.close()
    pool.join()
    end_time = time.time()
    
    # print("Fibonacci:", results[0])
    # print("Factorial:", factorial_result)
    # print("Squares:", squares_result)
    # print("Cubes:", cubes_result)
    print("Execution time:", round(end_time - start_time, ndigits=1), "seconds")

if __name__ == "__main__":
    main()