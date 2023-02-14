"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# open the file

emp_file = open("employee_data.csv", "r")
employee = csv.reader(emp_file)


# create an empty dictionary

emp_dict = {}

# use a loop to iterate through the csv file

for row in employee:
    Employee_Name = row[1] + " " + row[2]
    salary = row[5]
    clearance = row[9]

    # check if the employee fits the search criteria

    if clearance == "TS":
        print(f"Employee_Name: {Employee_Name} Current Salary: {salary}")
        emp_dict[Employee_Name] = float(salary) + float(salary) * 0.10


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image


for key, value in emp_dict.items():
    print(f"Employee Name: {key} New Salary: {value}")

print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.
