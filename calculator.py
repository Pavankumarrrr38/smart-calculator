def smart_calculator():
    print("Smart Calculator started. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("> ").strip()
            
            # Skip empty inputs
            if not user_input:
                continue
                
            # Exit condition
            if user_input.lower() == 'exit':
                print("Bye!")
                break
                
            # Safely evaluate the mathematical expression
            # using eval with builtins restricted for basic safety
            result = eval(user_input, {"__builtins__": None}, {})
            print(result)
            
        except SyntaxError:
            print("Invalid expression")
        except NameError:
            print("Unknown variable or unsupported operation")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except Exception:
            print("Error evaluating expression")

if __name__ == "__main__":
    smart_calculator()
