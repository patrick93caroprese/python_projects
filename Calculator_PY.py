#Defining variables
def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y

def power (x,y):
    return x ** y

def growth_rate (x,y):
    return ((y - x) / x) * 100


#Start building up the logic giving out the possible choices
print("Choose your calculation:")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
print("Power")
print("Growth Rate")

#Using a while loop for automatizing everything
while True:

    choice = input("Enter your choice: ")

    if choice.upper() in ("A","ADD","ADDITION",
                          "S","SUB","SUBTRACT","SUBTRACTION",
                          "M","MULT","MULTIPLY","MULTIPLICATION",
                          "D","DIV","DIVIDE", "DIVISION",
                          "P", "POWER",
                          "G", "GROWTH", "GROWTH RATE"):

        num_1 = float(input("Enter first number: "))

        num_2 = float(input("Enter second number: "))

        if choice.upper() in ("A","ADD","ADDITION"):
            print(num_1 , "+", num_2, "=", add(num_1,num_2))

        elif choice.upper() in ("S","SUB","SUBTRACT","SUBTRACTION"):
            print(num_1 , "-", num_2, "=", subtract(num_1,num_2))

        elif choice.upper() in ("M","MULT","MULTIPLY","MULTIPLICATION"):
            print(num_1 , "*", num_2, "=", multiply(num_1,num_2))

        elif choice.upper() in ("D","DIV","DIVIDE", "DIVISION"):
            print(num_1 , "/", num_2, "=", divide(num_1,num_2))

        elif choice.upper() in ("P", "POWER"):
            print(num_1, "to the power of", num_2, "=", power(num_1,num_2))

        elif choice.upper() in ("G", "GROWTH", "GROWTH RATE"):
            print("The growth rate from", num_1 , "to", num_2, "=", round(growth_rate(num_1,num_2),2), "%")

    #Logic in case of a typing error
    else:
        print("PLEASE TYPE THE CORRECT CHOICE")

    #Logic in case of a next calculation
    next_calculation = input("Wanna do another calculation?: ")

    #Logic for breaking the loop, ending the conversation
    if next_calculation.upper() in ("N", "NO", "NOPE", "NO WAY", "HELL NO", "THAT'S ENOUGH"):
        break