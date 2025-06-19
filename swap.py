
def swap_numbers():
    print("Number Swapper")
    print("--------------")
    
    # Get input from the user
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    print(f"\nBefore swapping: a = {a}, b = {b}")

    # Swap the values
    a, b = b, a

    print(f"After swapping: a = {a}, b = {b}")

if __name__ == "__main__":
    swap_numbers()
