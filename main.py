# =========================================
# Introduction
# =========================================

"""
Welcome to this calculator thingy. That's it.
"""

# =========================================
# Dependencies
# =========================================

import sympy as sp

# =========================================
# Global Variables
# =========================================

x = sp.symbols("x")
check = "n"
result_prev = {}
result = complex()
a1 = complex()
b1 = complex()

# =========================================
# Functions
# =========================================

# Arithmetic Calc
def arthimetic_all():
    print("Operations:")
    print("A = Addition")
    print("S = Subtraction")
    print("M = Multiplication")
    print("D = Division")
    b_choice = str(input("\nSelect an operation: ").lower())
    global a1
    global b1
    a1 = float(input("Enter the 1st number: "))
    b1 = float(input("Enter the 2nd number: "))

    if b_choice == "a":  # Operator Module
        result = a1 + b1
        print(f"\n{a1} + {b1} = {result}")
    elif b_choice == "s":
        result = a1 - b1
        print(f"\n{a1} - {b1} = {result}")
    elif b_choice == "m":
        result = a1 * b1
        print(f"\n{a1} * {b1} = {result}")
    elif b_choice == "d":
        result = a1 / b1
        print(f"\n{a1} / {b1} = {result}")

# Calculus Calc
def calculus_all():
    # If another letter typed, the module breaks because there isn't a fact-checker for operator module selectio
    print("Operations:")
    print("D = Derivative")
    print("I = Integral")
    a_choice = str(input("\nSelect an operation: ").lower())
    global a1
    a1 = input("Enter f(x): ")

    if a_choice == "d":  # Operator Module
        f = sp.sympify(a1)
        derivative = sp.diff(f, x)
        print(f"\nThe Derivative of '{f}' is: {derivative}")
    elif a_choice == "i":
        f = sp.sympify(a1)
        integral = sp.integrate(f, x)
        print(f"\nThe Integral of '{f}' is: {integral}")

# Options
#### def options_all():

# Restart
def restart():
    while True:
        print("---------------------")
        cont_choice = input("Restart? (Y/N): ").lower()
        if cont_choice == "y":
            print("---------------------")
            break
        elif cont_choice == "n":
            quit()

# # Function Solver Module
#     a = input("Enter f(x) equation: ")
#     b = sp.solvers(***) (?)

# =========================================
# Main Program Loop
# =========================================

# Program Introduction
print("****************************")
print("   Welcome to 'Mathetron'")
print("****************************")

while True:
    # Mode Selection
    print("\nCalculation Modes:")
    print("Enter '1' for Calculus")
    print("Enter '2' for Arithmetic")
    print("Enter '3' for Algebra | Function Solver (IP)")
    # Slope calculator given a f(x)?

    # Program Options
    print("\nOptions:")
    print("Enter 'Q' to Quit")
    print("Enter 'C' to Clear")
    print("Enter 'A' to Combine Previous Result (IP)")

    # Choice Selection
    choice = input("\nEnter your choice: ").lower()
    print("---------------------")

    # Option Selection
    #### options_all()
    if choice == "q":  # Quit Module
        check = "y"
        quit()
    if choice == "c":  # Clear Module
        check = "y"
        print("\n" * 50)
        # [combine, result, a1, b1, a2] = 0
    if choice == "a":  # Combiner Module
        check = "y"
        a1 = result
        print(a1, result)
        print("Select another calculation you wish to combine with")
        # a2 becomes a1 in below calculations but this would need to be in a or the loop for calculations
        # Then you can just make the calculation with a and b with the new a2 input replacing a1 input
    #####

    # Calculation Selection
    if choice in ("1", "2"):
        if choice == "1":
            calculus_all()
        elif choice == "2":
            arthimetic_all()
        restart()
    elif check == "n":
        print("Invalid choice. Please select an option or mode.")

    # Variable Reset
    check = "n"

# =========================================
