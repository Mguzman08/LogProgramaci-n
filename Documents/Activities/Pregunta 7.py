#Algorythm to calcule the total amount to be paid for a Fumigation service.
#We will define the functions to determine the possible discounts.

def discount1(total):
    return total * 0.95
def discount2(total):
    outstanding = total - 3000
    Discount = outstanding * 0.10
    return total - Discount

#We will ask the user to enter the details name, area to fumigate (hectares) 
# and the type of fumigation (1, 2, 3 or 4).

name = input("Enter the name of the client: ")
area = float(input("Enter the area to fumigate (hectares): ")) 
type_fumigation = int(input("Enter the type of fumigation (1:Weeds, 2:Lobsters, 3:Worms or 4:All of the above): "))

#We would like to be sure the type of fumigation is correct, if not we will ask the user to enter it again.
while type_fumigation < 1 or type_fumigation > 4:
    print("Invalid type of fumigation, please enter a valid type (1, 2, 3 or 4).")
    type_fumigation = int(input("Enter the type of fumigation (1:Weeds, 2:Lobsters, 3:Worms or 4:All of the above): "))

#We will calculate the total amount to be paid based on the area and type of fumigation.
if type_fumigation == 1:    
    total = area * 10
elif type_fumigation == 2:
    total = area * 15      
elif type_fumigation == 3:
    total = area * 20
else:
    total = area * 30

#We will apply the discounts based on the total amount to be paid.
if area > 10000:
    total = discount1(total)
elif total > 3000:
    total = discount2(total)

#We will print the name and total amount to be paid for the fumigation service.
print(f"Client: {name}")
print(f"Total amount to be paid: ${total:.2f}")
