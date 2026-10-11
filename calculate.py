import logging
logging.basicConfig(level=logging.INFO)

def calculate(a, b, operation):
    logging.info("Calculating %s %s %s", a, operation, b)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Inputs must be numbers"

    if operation == 'add':
        return {"result": a + b}
    elif operation == 'subtract':
        return {"result": a - b}
    elif operation == 'multiply':
        return {"result": a * b}
    elif operation == "divide":
        if b == 0:
            return {"error": "Cannot divide by zero"}
        return {"result": a / b}
    elif operation == "power":
        return {"result": a ** b}
    elif operation == "modulo":
        if b == 0:
            return {"error": "Cannot divide by zero"}
        return {"result": a % b}

# Example usage
if __name__ == "__main__":
    print(calculate(5, 3, 'add'))        # Output: 8
    print(calculate(5, 3, 'subtract'))   # Output: 2
    print(calculate(5, 3, 'multiply'))   # Output: 15
    print(calculate(5, 3, 'divide'))     # Output: 1.666...
    print(calculate(5, 0, 'divide'))     # Error