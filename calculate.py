def calculate(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    elif operation == "power":
        return a ** b

# Example usage
if __name__ == "__main__":
    print(calculate(5, 3, 'add'))        # Output: 8
    print(calculate(5, 3, 'subtract'))   # Output: 2
    print(calculate(5, 3, 'multiply'))   # Output: 15
    print(calculate(5, 3, 'divide'))     # Output: 1.666...
    print(calculate(5, 0, 'divide'))     # Error