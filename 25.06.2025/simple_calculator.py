# Filename: simple_calculator.py
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Division by zero error!"
        return num1 / num2
    else:
        return "Invalid operator"

result = calculator(10, 5, '+')
print(result) # Output: 15

result = calculator(10, 5, '/')
print(result) # Output: 2.0

result = calculator(10,0,'/')
print(result) #Output: Division by zero error!