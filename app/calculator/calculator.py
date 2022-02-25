def calc(val1, operation, val2):

    if operation == "+":
        return val1 + val2

    elif operation == "-":
        return val1 - val2

    elif operation == "*":
        return val1 * val2

    elif operation == "/":
        return val1 / val2

    elif operation == "%":
        return val1 % val2

    elif operation == "**":
        return val1 ** val2
    
    elif operation == "//":
        return val1 // val2

    else:
        print("Invalid or undefined operator!")