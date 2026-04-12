# Odd numbers sum
# We ask the user for a number
N = int(input("Enter a positive integer: "))

suma = 0

for i in range(1, N + 1):
    if i % 2 != 0:
        suma += i

print(f"The sum of odd numbers from 1 to {N} is: {suma}")