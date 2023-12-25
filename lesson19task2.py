# Task 2

# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 'start', 'end', and optional step. 
# Tips: See the documentation for 'range' function


def in_range(start, end, step=1):
    result = []
    if step == 0:
        raise ValueError("Step cannot be zero")
    
    current = start
    while (current < end):
        result.append(current)
        current += step

    return result

print(in_range(1,25,2))