# # ---------------------------------------------------------- #
# # Title: Listing01Module
# # Description: Components of a typical module
# # ChangeLog (Who,When,What):
# # RRoot,1.1.2030,Created started script
# # ---------------------------------------------------------- #
#
# def standalone_function():
#     print("Called standalone_function")
#
# class MyData:
#     def __init__(self):
#         print("Created MyData object")
#
# class FileProcessor:
#
#     @staticmethod
#     def process_data():
#         print("Called process_data")
#
# class IO:
#
#     @staticmethod
#     def print_data():
#         print("Called print_data")
# # ---------------------------------------------------------- #
# # Title: Listing02
# # Description: A script that uses a module
# # ChangeLog (Who,When,What):
# # RRoot,1.1.2030,Created started script
# # ---------------------------------------------------------- #
# import Listing01Module
#
# # Calling a standalone function
# Listing01Module.standalone_function()
#
# # Creating an object from a class
# objMD = Listing01Module.MyData()
#
# # Calling static methods in two classes
# Listing01Module.FileProcessor.process_data()
# Listing01Module.IO.print_data()
# # ---------------------------------------------------------- #
# # Title: Listing03
# # Description: A script that runs as the "Main" module
# # ChangeLog (Who,When,What):
# # RRoot,1.1.2030,Created started script
# # ---------------------------------------------------------- #
# print(__name__)
# if __name__ == "__main__":
#     print("This file is the starting point of my program!")
# # ---------------------------------------------------------- #
# # Title: Listing 04
# # Description: A script module that should be run as "Main"
# # ChangeLog (Who,When,What):
# # RRoot,1.1.2030,Created started script
# # ---------------------------------------------------------- #
# if __name__ == "__main__":
#     import Listing01Module
# else:
#     raise Exception("This file was not created to be imported")
# # ---------------------------------------------------------- #
# # Title: Listing 05
# # Description: A script module that should not run as "Main"
# # ChangeLog (Who,When,What):
# # RRoot,1.1.2030,Created started script
# # ---------------------------------------------------------- #
# if __name__ == "__main__":
#     raise Exception("This file is not meant to ran by itself")
# # ---------------------------------------------------------- #
# # Title: Listing 06
# # Description: A module of data classes
# # ChangeLog (Who,When,What):
# # RRoot,1.1.2030,Created started script
# # ---------------------------------------------------------- #
# if __name__ == "__main__":
#     raise Exception("This file is not meant to ran by itself")
#
# class Person:
#     """Stores data about a person:
#
#     properties:
#         first_name: (string) with the persons's first name
#
#         last_name: (string) with the persons's last name
#     methods:
#         to_string() returns comma separated product data (alias for __str__())
#     changelog: (When,Who,What)
#         RRoot,1.1.2030,Created Class
#     """
#
#     # -- Constructor --
#     def __init__(self, first_name, last_name):
#         # -- Attributes --
#         self.__first_name = first_name
#         self.__last_name = last_name
#
#     # -- Properties --
#     @property
#     def first_name(self):
#         return str(self.__first_name).title()
#
#     @first_name.setter
#     def first_name(self, value):
#         if not str(value).isnumeric():
#             self.__first_name = value
#         else:
#             raise Exception("Names cannot be numbers")
#
#     @property
#     def last_name(self):
#         return str(self.__last_name).title()
#
#     @last_name.setter
#     def last_name(self, value):
#         if not str(value).isnumeric():
#             self.__last_name = value
#         else:
#             raise Exception("Names cannot be numbers")
#
#     # -- Methods --
#     def to_string(self):
#         """ Explicitly returns a string with this object's data """
#         return self.__str__()
#
#     def __str__(self):
#         """ Implicitly returns a string with this object's data """
#         return self.first_name + ',' + self.last_name
# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import Listing06 as D  # data classes
    import Listing07 as P  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Test IO classes
# TODO: create and test IO module