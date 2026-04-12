# Powers calculator
# We ask the user for a list of numbers
entrada = input("Enter positive integers separated by commas: ")
numbers = [int(x) for x in entrada.split(",")]

for num in numbers:
    print(f"\nNumber: {num}")
    print(f"  Square root: {num ** 0.5:.2f}")
    print(f"  Square: {num ** 2}")
    print(f"  Cube: {num ** 3}")