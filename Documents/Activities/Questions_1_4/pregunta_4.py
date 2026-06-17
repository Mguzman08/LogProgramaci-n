# Max and min sum
# We ask the user for a list of numbers
entrada = input("Enter positive numbers separated by commas: ")
numbers = [float(x) for x in entrada.split(",")]

maximo = max(numbers)
minimo = min(numbers)

print(f"Max: {maximo}")
print(f"Min: {minimo}")
print(f"Sum: {maximo + minimo}")