## **Dev:** *Kellen Hunter*  
## **Date:** *09/03/20*  

# Assignment 9 - Connecting Modules Together

## Introduction  

This week I learned how to write code once and use it over and over again. Modules are helpful to break up code into separate sections. This helps the coder organize code better so it can modified quicker. A module cam define functions, variables and classes. The import statement is used to call up modules into the “main” python file. This file is where the main body of the code is stored.  

```
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
```

![Working in PyCharm 1](https://kbhunter5.github.io/IntroToProg-Python-Mod09/docs/PyCharmPic1.png "Working in PyCharm 1")
![Working in PyCharm 1](https://github.com/kbhunter5/IntroToProg-Python-Mod09/blob/master/doc/PyCharmPic1.png "Working in PyCharm 1")

### Picture of code working in Working in PyCharm 1.

![Working in PyCharm 2](https://kbhunter5.github.io/IntroToProg-Python-Mod09/docs/PyCharmPic2.png "Working in PyCharm 2")
![Working in PyCharm 2](https://github.com/kbhunter5/IntroToProg-Python-Mod09/blob/master/doc/PyCharmPic2.png "Working in PyCharm 2")
### Picture of code working in Working in PyCharm 2.

![Employee Data.txt](https://kbhunter5.github.io/IntroToProg-Python-Mod09/docs/CommandPrompt.png "Employee Data.txt")
### Picture of the Employee Data.txt outputfile

![Command Prompt Pic](https://kbhunter5.github.io/IntroToProg-Python-Mod09/docs/CommandPrompt.png "Command Prompt Pic")
### Picture of code working in the Command Prompt.

## Summary

This week I was able to separate my code into separate modules and call up those modules into a main script. The separate modules helped me organize my code better. So when something needed to be updated or changed I could quickly access the correct module update the code and rerun. Saving these modules as template could help a coder finish project faster.  

## Sources
https://www.w3schools.com/python/python_modules.asp  
https://www.geeksforgeeks.org/python-locals-function/  
https://realpython.com/python-modules-packages/  
https://www.tutorialspoint.com/python/python_modules.htm  
