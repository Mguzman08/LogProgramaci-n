#Algorythm to analize the temperature during a month and determine the average temperature, 
# the highest and lowest temperature, 
# and the number of days with temperatures above and below the average.

#We will first, create the list where will store the temperatures of each day of the month.
temperatures = []

#We will ask the user to enter the temperatures of each day of the month.
for i in range(1, 31):
    temp = float(input(f"Enter the temperature for day {i}: "))
    temperatures.append(temp)

#We will calculate the average temperature.
average = sum(temperatures) / len(temperatures)

#We will find the highest and lowest temperatures.
highest = max(temperatures)
lowest = min(temperatures)

#We will count the number of days with temperatures above and below the average.
above_average = 0
below_average = 0

for temp in temperatures:
    if temp > average:
        above_average += 1
    elif temp < average:
        below_average += 1

#We will print the results.
print(f"Average temperature: {average:.2f}")
print(f"Highest temperature: {highest}")
print(f"Lowest temperature: {lowest}")
print(f"Days with temperature above average: {above_average}")
print(f"Days with temperature below average: {below_average}")