# MySQL API
# MySQL API Documentation: https://dev.mysql.com/doc/connector-python/en/
from time import sleep
from getpass import getpass
import mysql.connector
import os

from numpy import disp

# Debugging purposes
connecting = True

# 
displayLength = 80
formatCenter = "| {:^76} |"
formatLeft = "| {:<76} |"

print("Connecting to database...\n")

# Method to connect to MySQL server
# See https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html for list of arguements

if connecting:
    try:
        cnx = mysql.connector.connect(user=input("Enter username: "), password=getpass(prompt="Enter password: "), host=input("Enter host: "), database=input("Enter database name: "))
    except mysql.connector.Error as err:
        if err.errno == err.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username or password is incorrect...\nRun the script again...")
            exit()
        elif err.errno == err.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist...\nRun the script again...")
            exit()
        else:
            print(err)
            print("Run script again...")
            exit()

# curser() instantiates objects that can execute operations such as SQL statements. Interacts with MySQL server through MySQLConnection object
# Visit https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html for full documentation
if connecting:
    cursor = cnx.cursor()

# Clears console
def clearConsole():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

# Exits the program. Option # 9
def onExit():
    clearConsole()
    if connecting:
        cursor.close()
        cnx.close()
    print('Quiting program...')
    print('Thanks for using Forbidden Cucumber Knowledge software! Good bye!')
    exit()

def optionONE():
    # Search a computer with its computerID and check and show if its available
    print("-" * displayLength)
    print(formatCenter.format("**** Check if particular computer is available ****"))
    print(formatLeft.format("To check if a computer is available, please the computer's ID"))
    
    # Make sure input is valid
    while True:
        try:
            computerID = int(getpass(prompt=(formatLeft.format("Enter computer ID: "))))
        except ValueError as err:
            print(formatLeft.format("Oops! That was not a valid number. Please try again..."))
            continue
        break
    
    print(formatLeft.format("Searching for computer of ID: " + str(computerID)))
    
    # SQL query: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    # Return all of the available computers
    outerQuery = ("SELECT C.comp_id, C.comp_loc "
                  "FROM computers AS C "
                  "WHERE C.comp_id NOT IN (SELECT CU.c_comp_id FROM computeruse AS CU)")
    cursor.execute(outerQuery)
    rows = cursor.fetchall()
    
    # Check list of all available computers to see if specific computer is available
    for (comp_id, comp_loc) in rows:
        if comp_id == computerID:
            print(formatLeft.format("Computer {id} is available on the {floor}".format(id=computerID, floor=comp_loc)))
            return
    
    print(formatLeft.format("Computer {id} is unavailable.".format(id=computerID)))        
    input(formatLeft.format("Press 'enter' to go back to menu"))
    print(("-" * displayLength) + "\n")
    
def optionTWO():
    # show the list of available computers
    print("-" * displayLength)
    print(formatCenter.format('**** List of available computers ****'))

    #**SQL QUERY of the list of available computers, show computerID and location**
    outerQuery = ("SELECT C.comp_id, C.comp_loc "
                "FROM computers AS C "
                "WHERE C.comp_id NOT IN (SELECT CU.c_comp_id FROM computeruse AS CU)")
    cursor.execute(outerQuery)
    rows = cursor.fetchall()
    
    # Check to see if there are no returned rows
    if (len(rows) == 0):
        print(formatLeft.format("There are no available computers"))
    else:
        # Print out all available computers
        for (comp_id, comp_loc) in rows:
            print(formatLeft.format("Computer {id} is available on floor {floor}".format(id=comp_id, floor=comp_loc)))
            return

    input(formatLeft.format("Press 'enter' to go back to menu"))
    print(("-" * displayLength) + "\n")

#def optionTHREE(): skip it for now

def optionFOUR():
    # Check if a selected room is available
    print("-" * displayLength)
    print(formatCenter.format('**** Checking if a particular room is available ****'))
    print(formatLeft.format('To check if a room is available, please enter room number.'))
    while True:
        try:
            roomNumber = int(getpass(prompt=formatLeft.format("Enter room number: ")))
        except ValueError as err:
            print(formatLeft.format("Oops! That was not a valid number. Please try again..."))
            continue
        break
    #SQL query of room number and room floor
    outerQuery = ("SELECT R.room_num, R.floor "
                  "FROM rooms AS R "
                  "WHERE R.room_num NOT IN (SELECT RU.r_room_num FROM roomuse AS RU)")
    cursor.execute(outerQuery)
    rows = cursor.fetchall()
    
    for (room_num, floor) in rows:
        if (room_num == roomNumber):
            print(formatLeft.format("Room {id} is available on floor {num}".format(id=room_num, num=floor)))
            return
    
    print(formatLeft.format("Room {id} is unavailable.".format(id=roomNumber)))        
    input(formatLeft.format("Press 'enter' to go back to menu"))
    print(("-" * displayLength) + "\n")
    
def optionFIVE():
    # Show list of available rooms
    print("-" * displayLength)
    print(formatCenter.format('**** List of available rooms ****'))
    
    #SQL query showing the LIST of available rooms, show its room number and floor
    outerQuery = (
                "SELECT R.room_num, R.floor "
                "FROM rooms AS R "
                "WHERE R.room_num NOT IN (SELECT RU.r_room_num FROM roomuse AS RU)"
                )
    cursor.execute(outerQuery)
    rows = cursor.fetchall()
    
    if (len(rows) == 0):
        print("There are no available rooms")
    else:
        for (room_num, floor) in rows:
            print(formatLeft.format("Room {id} is available on floor {num}".format(id=room_num, num=floor)))
    
    input(formatLeft.format("Press 'enter' to go back to menu"))
    print(("-" * displayLength) + "\n")

def optionSIX():
    # Check if a book is in stock or not
    queryList = []
    print("-" * displayLength)
    print(formatCenter.format('**** Checking if book is in stock ****'))
    print(formatLeft.format('To check if a book is in stock, please enter book ISBN(13-digit)'))

    while True:
        try:
            bookISBN = (getpass(prompt=(formatLeft.format("Enter book ISBN(13-digit): "))))
        except ValueError as err:
            print(formatLeft.format("Oops! That was not a valid number. Please try again..."))
            continue
        break
    print(formatLeft.format("Checking to see if a book with ISBN " + bookISBN + " exists..."))
    queryList.append(bookISBN)

    #SQL query show book-ISBN, booktitle, book-author, book-quantityinstock, book-location
    outerQuery = (
            "SELECT B.title, A.afname, A.alname, B.isbn, B.stock, B.location "
            "FROM books AS B, authors AS A "
            "WHERE B.baid = A.aid and %s = B.isbn"
            )
    
    cursor.execute(outerQuery, queryList)
    rows = cursor.fetchall()
    
    if (len(rows) == 0):
        print(formatLeft.format("We could not find a book with ISBN: {id}".format(id=bookISBN)))
    else:
        # Change when not tired
        for (title, fname, lname, isbn, stock, location) in rows:
            print(formatLeft.format("{t}, {name}, {id}, {s}, {l}".format(t=title, name=(lname + ", " + fname), id=isbn, s=stock, l=location)))
    
    input(formatLeft.format("Press 'enter' to go back to menu"))
    print(("-" * displayLength) + "\n")

def optionSEVEN(): #SKIP FOR NOW
    print(formatCenter.format('**** Checking if book is due ****'))
    print(formatLeft.format('To check if a book is due, please enter in userID.'))

def optionEIGHT():
    print(formatCenter.format('**** Search up book ****'))
    print(formatLeft.format('To look for a book, please insert some info that relates to the searching book.'))
    print(formatLeft.format('You can look up a book by its book-title, book-author, book-ISBN(13-digit), AND OR book-Publication Date.'))

        
# Handles input by assigning options to functions
# Must define the functions before this
input_handler = {
    1 : optionONE, # TODO: Inplement options 
    2 : optionTWO,
    3 : "do option 3",
    4 : optionFOUR,
    5 : optionFIVE,
    6 : optionSIX, 
    7 : "do option 7",
    8 : "do option 8",
    9 : onExit
}

if __name__ == "__main__":
    clearConsole()
    while True:
        # clearConsole() 
        # Useful documenation about Python string formatting: https://docs.python.org/3/library/string.html and https://www.w3schools.com/python/ref_string_format.asp
        print("-" * displayLength)
        print(formatCenter.format("**** Library Menu ****"))
        print(formatLeft.format("1) Check if a particular computer is available"))
        print(formatLeft.format("2) See the list of available computers"))
        print(formatLeft.format("3) See available apps on computers"))
        print(formatLeft.format("4) Check if a particular room is available"))
        print(formatLeft.format("5) See the list of available rooms"))
        print(formatLeft.format("6) Check if a book is in stock"))
        print(formatLeft.format("7) Check when book is due"))
        print(formatLeft.format("8) Search for book"))
        print(formatLeft.format("9) Quit"))
        print("-" * displayLength)

        # Error handling
        while True:
            try:
                menuChoice = int(input("Please enter an option: "))

            except ValueError as err:
                print("Oops! That was not a valid number. Please try again...")
                continue

            if (menuChoice < 1 or menuChoice > 9):
                print("Invalid option. Please try again...")
            else:
                break

        # Handles user input by calling appropriate function
        input_handler[menuChoice]()
