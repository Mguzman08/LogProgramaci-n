#Pitagora´s algorithm
#1. We will ask to the user to enter a list of numbers. 

entrada = input("Enter a list of numbers separated by commas: ")
#2. We will then, convert the numbers in a list. 
numbers = [float(x) for x in entrada.split(",")]

exitos = 0
cantidad_numbers = len(numbers) #We will store the quantity of numbers in a variable to use it in the nested loops.

#3. The nested loops development 

for i in range(cantidad_numbers):
    for j in range(i + 1, cantidad_numbers):
        for k in range(j + 1, cantidad_numbers):

            #We will define the current triple

            triple=[numbers[i], numbers[j], numbers[k]]

            #We will order the triple in ascending order (c the highest value, a and b the lowest values)
            triple.sort()
            a = triple[0]
            b = triple[1]
            c = triple[2]

            #We will verify the Pythagorean condition with the ordered triple and possible combinations of a, b, c.
            if round (a**2 + b**2, 10) == round (c**2, 10): #We will round the values to avoid issues with floating point precision.
                print(f"{a}, {b}, {c} form a Pythagorean triplet.")
                exitos += 1

#4. Finally, we will print the total number of Pythagorean triplets found.
print(f"Total Pythagorean triplets found: {exitos}")

#code made with help of gemini, the AI assistant of Google, using nested loops (I learned how to use it for future projects)
#and the Pythagorean theorem to find triplets of numbers that satisfy the condition a^2 + b^2 = c^2.
