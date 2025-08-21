# ---------------- Basic Calculator App ----------------
# This program performs 4 basic operations: addition, subtraction, 
# multiplication, and division. The user selects an operation, 
# enters two numbers, and the result is displayed.

# ---------------- Operations Functions ----------------
# Each function takes the global variables no1 and no2 
# and performs the chosen operation.


def add():
    print(no1+no2)

def subtract():
    print(no1-no2)

def multiply():
    print(no1*no2)

def divide():
    if no2==0:
        print("Cant Be divided by 0 try another no please.........")
    print(no1/no2)



while True:
    print("----------------Basic Calculator App----------------")    

    #options 
    print("""
    Enter 1 to Add 
    Enter 2 to Subtract
    Enter 3 to Multiply
    Enter 4 to Divide 
    Enter 5 to Exit """)

    #taking choice input
    choice=int(input("Enter you choice from 1 to 5 : "))

    if choice == 5 :
        print("----------------Thanks for using Calculator----------------")
        break

    #taking operands
    no1=int(input("Enter no1 : "))
    no2=int(input("Enter no1 : "))

    #calling function as per the choice
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4 :
        divide()
