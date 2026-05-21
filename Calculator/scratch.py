def format_num(x):
    if x == int(x):
        return str(int(x))
    else:
        return "{:.2f}".format(x)

print("Simple Calculator (type 'exit' at any prompt to quit)")

while True:
    no1_str = input("\nEnter first number: ").strip()
    if no1_str.lower() == 'exit':
        break
    try:
        no1 = float(no1_str)
    except ValueError:
        print("Error: Please enter a valid number")
        continue

    no2_str = input("Enter second number: ").strip()
    if no2_str.lower() == 'exit':
        break
    try:
        no2 = float(no2_str)
    except ValueError:
        print("Error: Please enter a valid number")
        continue

    op = input("Enter operator (+, -, *, /, %, **, ^): ").strip()
    if op.lower() == 'exit':
        break

    if op == '^':
        op = '**'

    try:
        if op == '+':
            result = no1 + no2
        elif op == '-':
            result = no1 - no2
        elif op == '*':
            result = no1 * no2
        elif op == '/':
            result = no1 / no2
        elif op == '%':
            result = no1 % no2
        elif op == '**':
            result = no1 ** no2
        else:
            print(f"Error: Unsupported operator '{op}'. Valid operators: +, -, *, /, %, **, ^")
            continue
        
        display_no1 = format_num(no1)
        display_no2 = format_num(no2)
        result_str = format_num(result)
        print(f"\n{display_no1} {op} {display_no2} = {result_str}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except (OverflowError, ValueError) as e:
        print(f"Math Error: {e}")

print("\nCalculator closed. Goodbye!")