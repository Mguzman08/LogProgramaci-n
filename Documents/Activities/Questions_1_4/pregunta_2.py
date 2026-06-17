# Standard deviation
# We ask the user for a list of numbers
entrada = input("Enter numbers separated by commas: ")
numbers = [float(x) for x in entrada.split(",")]

mean = sum(numbers) / len(numbers)

variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std_deviation = variance ** 0.5

print(f"Mean: {mean:.2f}")
print(f"Standard deviation: {std_deviation:.2f}")