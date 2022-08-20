"""This programme uses the program Calculations.py
    as a module and to use it we have to import it as a normal module.


    This programme is a menu driven programme that has two major components
    the first component begin the basic calculation part and the second
    component does the scientific calculations.
"""
import Calculations

while True:
    print("!Welcome to the calculator!")
    print("1. Basic Calculations")
    print("2. Scientific Calculations")
    print("3. Exit")
    choice1 = int(input("Enter your choice: "))

    if choice1 == 1:
        print("This are the basic calculations:\n")
        print("1. Addition")
        print("2. Subtractions")
        print("3. Multiplication")
        print("4. Divison")
        print("5. Floor Divison")
        print("6. Modulus")
        print("7. Absolute value")
        print("8. Factorial")
        print("9. Power")
        print("10. GCD")

        choice2 = int(input("Enter the basic calculation to be performed: "))

        if choice2 == 1:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The addition of two numbers gives us: ",Calculations.add(x, y))

        elif choice2 == 2:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The subtraction of two numbers gives us: ", Calculations.subtract(x, y))

        elif choice2 == 3:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The mulitplication of two numbers gives us: ", Calculations.multiply(x, y))
        
        elif choice2 == 4:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The division of two numbers gives us: ", Calculations.divide(x, y))
        
        elif choice2 == 5:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The floor division of two numbers gives us: ", Calculations.floordiv(x, y))
        
        elif choice2 == 6:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The modulus of two numbers gives us: ", Calculations.modulus(x, y))
        
        elif choice2 == 7:
            x = int(input("Enter a number: "))
            print("The absolute value of the numbers is: ", Calculations.absolute(x))
        
        elif choice2 == 8:
            x = int(input("Enter a number: "))
            print("The factorial of the numbers is: ", Calculations.fact(x))
        
        elif choice2 == 9:
            x = int(input("Enter a number: "))
            y = int(input("Enter the power: "))
            print("The power of the numbers is: ", Calculations.power(x, y))
        
        elif choice2 == 10:
            x = int(input("Enter a number: "))
            y = int(input("Enter a number: "))
            print("The GCD of two numbers is: ", Calculations.gcd(x, y))
        
        else:
            print("Enter a valid choice!")

    elif choice1 == 2:
        print("1. Natural Log")
        print("2. Base-10 Log")
        print("3. Base-2 Log")
        print("4. Sine value")
        print("5. Cosine value")
        print("6. Tan value")
        print("7. Hyperbolic Sine value")
        print("8. Hyperbolic Cosine value")
        print("9. Hyperbolic Tan value")
        print("10. Gamma value")

        choice3 = int(input("Enter the scientific calculation to be performed: "))

        if choice3 == 1:
            x = int(input("Enter a number: "))
            print("The natural log of the number is: ",Calculations.nlog(x))
        
        elif choice3 == 2:
            x = int(input("Enter a number: "))
            print("The base-10 log of the number is: ", Calculations.log_10(x))
        
        elif choice3 == 3:
            x = int(input("Enter a number: ")) 
            print("The base-2 log of the number is: ", Calculations.log_2(x))
        
        elif choice3 == 4:
            x = int(input("Enter a number: "))
            print("The Sine value of the number is: ", Calculations.Sin(x))
        
        elif choice3 == 5:
            x = int(input("Enter a number: "))
            print("The Cosine value of the number is: ", Calculations.Cos(x))
        
        elif choice3 == 6:
            x = int(input("Enter a number: "))
            print("The Tan value of the number is: ", Calculations.Tan(x))
        
        elif choice3 == 7:
            x = int(input("Enter a number: "))
            print("The Hyberbolic Sine value of the number is: ", Calculations.Sinh(x))
        
        elif choice3 == 8:
            x = int(input("Enter a number: "))
            print("The Hyberbolic Cosine value of the number is: ", Calculations.Cosh(x))
        
        elif choice3 == 9:
            x = int(input("Enter a number: "))
            print("The Hyberbolic Tan value of the number is: ", Calculations.Tanh(x))
        
        elif choice3 == 10:
            x = int(input("Enter a number: "))
            print("The Gamma value of the number is: ", Calculations.Gamma(x))
        
        else:
            print("Enter a valid choice!")

    elif choice1 == 3:
        print("Thank you for using the Calculator!!")
        exit()
        

    else:
        print("Enter a valid choice!") 
        