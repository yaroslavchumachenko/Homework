import asyncio
import time

async def fibonacci(n):
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

async def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

async def squares(n):
    return [i**2 for i in range(1, n + 1)]

async def cubes(n):
    return [i**3 for i in range(1, n + 1)]

async def main():
    start_time = time.time()
    tasks = [
        fibonacci(10000),
        factorial(100000),
        squares(10000),
        cubes(100000)
    ]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    # fibonacci_result, factorial_result, squares_result, cubes_result = results
    # print("Fibonacci:", fibonacci_result)
    # print("Factorial:", factorial_result)
    # print("Squares:", squares_result)
    # print("Cubes:", cubes_result)
    print("Execution time:", round(end_time - start_time, ndigits=1), "seconds")
    

asyncio.run(main())