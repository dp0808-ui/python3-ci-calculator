import sys

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Mathematical Error: Division by zero is undefined.")
    return a / b

def parse_input(user_input: str):
    tokens = user_input.strip().split()
    if not tokens:
        return None, None
    return tokens[0].lower(), tokens[1:]

def repl():
    print("INTERACTIVE PYTEST CALCULATOR REPL CLI")
    while True:
        try:
            raw_data = input("calc> ")
            cmd, args = parse_input(raw_data)
            if cmd in ['exit', 'quit']:
                print("Exiting application loop. Goodbye!")
                break
            if cmd is None:
                continue
            if cmd not in ['add', 'sub', 'mul', 'div']:
                print(f"Syntax Error: Unknown command '{cmd}'.")
                continue
            if len(args) != 2:
                print(f"Argument Error: '{cmd}' requires exactly 2 numerical parameters.")
                continue
            num1, num2 = float(args[0]), float(args[1])
            if cmd == 'add': res = add(num1, num2)
            elif cmd == 'sub': res = subtract(num1, num2)
            elif cmd == 'mul': res = multiply(num1, num2)
            elif cmd == 'div': res = divide(num1, num2)
            print(f"Result: {res:g}")
        except ValueError as math_err:
            print(f"Execution Error: {math_err}")
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupt signal caught. Goodbye!")
            break

if __name__ == "__main__":
    repl()
