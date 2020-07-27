# Open a new Jupyter Notebook.
# Create a list and assign it to employees.
# Create three nested lists in employees to store the information of each employee, respectively.
# Print the employees variable.
# Print the details of all employees in a presentable format.
# Print only the details of Lisa Crawford.

# we would start by creating a dummy list for employees

employees = [['John Mark', 38, 'sales'], ['Lisa Crawford',
                                          29, 'Marketing', ['Susan Petal', 34, 'Accounting']]]
print(employees)
# Next, we can utilize the for..in loop to print each of the record's data within employee:

for employee in employees:
    print(employee)

    # To have the data presented in a structured version of the employee record, add the following lines of code:
    for employee in employees:
        print("Name:", employee[0])
    print("Age:", employee[1])
    print("Department:", employee[2])
    print('-' * 20)

    # Lastly, if we were to print the details of Lisa Crawford, we would need to use the indexing method. Lisa's record is in position 1, so we would write:
