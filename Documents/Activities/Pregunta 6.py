#Calculator of payroll

#We will define some functions to calculate the payroll 
# of an employee based on their total salary and number of children.

def salary299(salary, children):
    porcentage = (6 - children) / 2
    return salary * (porcentage/100)

def salary300(salary, children):
    if children < 3:
        return salary * 0.03
    else:
        porcentage = (10 / children)
        return salary * (porcentage/100)
    
#We will ask the user to enter the total of hours worked and the number of children.
hours_worked = float(input("Enter the total of hours worked: "))
children = int(input("Enter the number of children: "))

Total_salary = hours_worked * 2000
Retention = 0
Subsidy = children * 1200

#We will calculate the retention and subsidy based on the total salary and number of children.
if Total_salary < 300000:
    if children >= 6:
        Retention = salary299(Total_salary, children)
    else:
        Retention = 0    
else:
    Retention = salary300(Total_salary, children)   

#We print the total salary, retention, subsidy and the salary to receive.

Salary_toreceive = Total_salary - Retention + Subsidy

print(f"The total salary is: {Total_salary}")
print(f"The retention is: {Retention}")     
print(f"The subsidy is: {Subsidy}")
print(f"The salary to receive is: {Salary_toreceive}")    