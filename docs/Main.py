# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Kellen Hunter 09/02/2020, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
strChoice = "" # Captures the user option selection
strStatus = "" # Captures status of users menu selection

# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
    import Listing07 as P  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
# TODO: create and test IO module

Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt") # Load data from file into a list of employee objects when script starts
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

while (True):
    #Eio.print_current_list_items(lstTable) # Show current data in the list/table
    Eio.print_menu_items() # Show user a menu of options
    strChoice = Eio.input_menu_options()  # Get user's menu option choice

    if strChoice == '1':  # Add a new Task
        Eio.print_current_list_items(lstTable)# Show user current data in the list of employee objects
        continue # to show the menu

    elif strChoice == '2': #add new employee data
        print(Eio.input_employee_data()) # print new employee
        continue # to show the menu

    elif strChoice == '3':  # # let user save current data to file
        #p.save_data_to_file("PersonData.txt", lstTable)
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        lstFileData = Fp.read_data_from_file("EmployeeData.txt")
        lstTable.clear()
        for line in lstFileData:
            lstTable.append(Emp(line[0], line[1], line[2].strip()))
        for row in lstTable:
            print(row.to_string(), type(row))
        continue # to show the menu
        # Let user exit program

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # Exit Program