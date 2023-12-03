def make_operation(operation_char, *numbers):
    result = 0
    if operation_char == "+":
        for i in numbers:
            result += i
    elif operation_char == "-":
        for i in numbers:
            result -= i
    elif operation_char == "*":
        result += numbers[0]
        for i in numbers:
            if i == result:
                pass
            else:
                result = result*i
    print(result)