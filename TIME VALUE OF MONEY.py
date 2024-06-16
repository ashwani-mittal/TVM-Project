#!/usr/bin/env python
# coding: utf-8

# # TIME VALUE MONEY ASSIGNMENT
# Includes vertical and Horizontal Financial Analytics


# First we need to import math and sys in order to make sure our packages support our codes. 
import math
# First find from the user which variable they wish to calculate
user= input("Hello. What are you wishing to calculate?\n 1.Please enter 'PreV' for present value.\n 2.Please enter 'FutV' for Future Value.\n 3.Please enter 'TP' for time period.\n 4.Please enter 'Int' for interest.\n").upper()
# I have above asked the user to put in inputs for all the variables that are in the equation. 
# I am neglecting n which is the compounding period because all the questions take n as annually.

# Now we are going to define all functions for each unknown by using names like PresentV, Time_Period, Rate_of_Interest, FutureV below one by one

def PresentV():
    # FUTUREV below represents the $$ Value of asset in future time
    FUTUREV = input("Please enter the future value: ")
    while True:
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            FUTUREV=float(FUTUREV)
            break
        except ValueError:
            FUTUREV=input("Invalid input here. Please enter a numerical value for Future Value: ")

    # Interest below represents the rate of interest as %
    Interest = input("Please enter the Interest rate: ")
    while True: 
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            Interest=float(Interest)
            break
        except ValueError:
            Interest=input("Invalid input here. Please enter a numerical value for Interest in %: ")

    # Time below represents the total time period in years
    TIME = input("Please enter period of time(this is in years): ")
    while True: 
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            TIME=float(TIME)
            break
        except ValueError:
            TIME=input("Invalid input here. Please enter a numerical value for Time Period: ")

    # PRESENTV Represents Imprudential, INC's present liability amount 
    # To get to the formula below, Solve FV = PV x [ 1 + (i / n) ] (n x t) for PV where n's \value is 1
    # PRESENTV = FUTUREV/(1 + Interest/100)^TIME
    # Divide the interest given by 100 to turn it from percent to decimal

    PRESENTV = FUTUREV / ((1 + Interest/100)**TIME)

    print("The present value is: %0.3f " % PRESENTV)

#---------------------------------------------------------------------------------------------------------------------------------------------

def Time_Period():
    # Interest below represents the rate of interest as %
    Interest = input("Please enter the Interest rate: ")
    while True: 
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            Interest=float(Interest)
            break
        except ValueError:
            Interest=input("Invalid input here. Please enter a numerical value for Interest in %")

    # PRESENTV below represents the $$ Value of asset in the present time
    PRESENTV = input("Please enter your present value: ")
    while True:
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            PRESENTV=float(PRESENTV)
            break
        except ValueError:
            PRESENTV=input("Invalid input here. Please enter a numerical value for Present Value")

    # FUTUREV below represents $$ Value of Asset in future time
    FUTUREV = input("Please enter your future value: ")
    while True:
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            FUTUREV=float(FUTUREV)
            break
        except ValueError:
            FUTUREV=input("Invalid input here. Please enter a numerical value for Future Value")

    # time represent the amount of years 
    # math.ceil() rounds up the time to mimimum number of years
    # because the interest is compounded annually. 
    # To get to the formula below, Solve FV = PV x [ 1 + (i / n) ] (n x t) for time where n's \value is 1
    # t = ln(FUTUREV/PRESENTV) / ln(1 + Interest/100)
    # Divide the interest given by 100 to turn it from percent to decimal

    time = math.ceil(math.log(FUTUREV/PRESENTV)/math.log(1 + Interest/100))

    print("The time period in years is: %d " % time)
    
#---------------------------------------------------------------------------------------------------------------------------------------------
    
def Rate_of_Interest():
    # Time below represents the time elapsed in Years
    TIME = input("Please enter period of time(this is in years): ")
    while True: 
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            TIME=float(TIME)
            break
        except ValueError:
            TIME=input("Invalid input here. Please enter a numerical value for Time Period")

    # PRESENTV below represents the $$ Value of asset in the present time
    PRESENTV = input("Please enter your present value: ")
    while True:
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            PRESENTV=float(PRESENTV)
            break
        except ValueError:
            PRESENTV=input("Invalid input here. Please enter a numerical value for Present Value")


    # FUTUREV below represents the $$ Value of asset in future time
    FUTUREV = input("Please enter your future value: ")
    while True:
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            FUTUREV=float(FUTUREV)
            break
        except ValueError:
            FUTUREV=input("Invalid input here. Please enter a numerical value for Future Value")

    # Interest represents the Annual Increase in Selling Price in Percent
    # To get to the formula below, Solve FV = PV x [ 1 + (i / n) ] (n x t) for i where n's \value is 1
    Interest = ((FUTUREV/PRESENTV)**(1/TIME)-1)*100

    print("The rate of interest is %0.3f percent" % Interest)
    
#---------------------------------------------------------------------------------------------------------------------------------------------

def FutureV():
    # PRESENTV below represents the $$ Value of asset in present time
    PRESENTV = input("Please enter present value: ")
    while True:
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            PRESENTV=float(PRESENTV)
            break
        except ValueError:
            PRESENTV=input("Invalid input here. Please enter a numerical value for Present Value")

    # Interest below represents the rate of interest as %
    Interest = input("Please enter the Interest rate: ")
    while True: 
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            Interest=float(Interest)
            break
        except ValueError:
            Interest=input("Invalid input here. Please enter a numerical value for Interest in %")

    # Time below represents the total time period in years
    TIME = input("Please enter period of time(this is in years): ")
    while True: 
        # Using try-except block below within while loop helps us to ensure numerical value is entered for our program.
        try:               
            TIME=float(TIME)
            break
        except ValueError:
            TIME=input("Invalid input here. Please enter a numerical value for Time Period")
            
    FUTUREV = PRESENTV * ((1 + Interest/100)**TIME)

    print("The future value is: %0.3f " % FUTUREV)

    
if user == 'PREV':
    PresentV()
elif user == 'FUTV':
    FutureV()
elif user == 'TP':
    Time_Period()
elif user == 'INT':
    Rate_of_Interest()
else:
    print("Your input is invalid. Please enter a valid input!")
    exit()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------