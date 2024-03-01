"""
Yara Hasan Alhourani: Wrote code for all the functions to convert from AED to other currencies. [aed_to_euro(money), aed_to_british_pound(money), aed_to_dollar(money)]
Wubrist Zewdie: Wrote code for all the functions to convert from Other currencies to AED. [euro_to_aed(amount), british_pound_to_aed(amount), dollar_to_aed(amount), others_to_aed()]
Afifa Monzur: Wrote code for the main menu, and submenus and remaining functions. [main_menu(), another_conversion(), exit(), aed_to_others()]
"""
euro_rate = 0.2513
pound_rate = 0.22
dollar_rate = 0.27
'''rate4=3.97
rate5=4.64
rate6=3.67'''

# This converts the amount from AED to Euro.
def aed_to_euro(money):
    """
    Converts the user input from AED to Euros.
    Parameter: money, float value, amount in AED.
    Returns amount in Euros.
    """
    euro = euro_rate * money
    print(money, "AED is equal to", euro, "GDP")
    another_conversion()


# This converts the amount from AED to Pound
def aed_to_british_pound(money):
    """
    Converts the user input from AED to pound.
    Parameter: money, float value, amount in AED.
    Returns amount in pound.
    """
    pound=pound_rate * money
    print(money,"AED is equal to",pound,"GDP")

# This converts the amount from AED to Dollar 
def aed_to_dollar(money):
    """
    Converts the user input from AED to dollar.
    Parameter: money, float value, amount in AED.
    Returns amount in dollar.
    """
    dollar=dollar_rate * money
    print(money,"AED is equal to",dollar,"GDP")

# This converts the amount from Euro to AED 
def euro_to_aed(amount):
    """
    Converts the user input from Euro to AED.
    Parameter: money, float value, amount in Euro.
    Returns amount in AED.
    """
    aed=amount/euro_rate 
    print(amount,"GDP is equal to",aed,"AED")

# This converts the amount from pound to AED
def british_pound_to_aed(amount):
    """
    Converts the user input from pound to AED.
    Parameter: money, float value, amount in pound.
    Returns amount in AED.
    """
    aed=amount/pound_rate
    print(amount,"GDP is equal to",aed,"AED")

# This converts the amount from dollar to AED
def dollar_to_aed(amount):
    """
    Converts the user input from dollar to AED.
    Parameter: money, float value, amount in dollar.
    Returns amount in AED.
    """
    aed=amount/dollar_rate 
    print(amount,"GDP is equal to",aed,"AED")

# convert submenu aed to other currency
def aed_to_others():
    money = float(input("Enter the amount you want to convert: "))
    print("\n 1. AED to Euro (EUR) \n 2. AED to British Pound (GBP) \n 3. AED to US Dollar (USD) \n")
    aed_to_other_selection = int(input("Enter the target currency from the above menu: "))
    try:
        if aed_to_other_selection == 1:
            aed_to_euro( money)
        if aed_to_other_selection == 2:
            aed_to_british_pound( money)
        if aed_to_other_selection == 3:
            aed_to_dollar( money)
    except:
        print("Error! Try again")
        aed_to_others()

# converts from other currency to AED
def others_to_aed():
    """
    the user will enter the amount they want to convert to
    """
    amount = float(input("Enter the amount you want to convert: "))

# displace introduction
def main_menu():
    """
    Displays the main menu of the Currency Converter program.

    Allows the user to choose between converting AED to other currencies,
    converting other currencies to AED, or exiting the program.
    """
    print("------------------------------")
    print("\t\"Main Menu\"")
    print("Welcome to Currency Converter")
    print("------------------------------")
    while True:
        print("\n 1. AED to other currencies \n 2. Other currencies to AED. \n 3. Exit \n")
        menu_selection = int(input("Enter the conversion direction - Choice(1/2/3): "))
        if menu_selection == 1:
            aed_to_others()
            break
        if menu_selection == 2:
            others_to_aed()
            break
        if menu_selection == 3:
            exit()
            break
        else:
            print("Invalid choice! Try again!")
            continue

# after the user chooses to do it again
def another_conversion():
    """
    Asks the user if they want to do another conversion and handles the response.
    Returns:
    bool: True if the user wants to do another conversion, False otherwise.
    """
    selection = input("Do you want to do another conversion? (y/n): ")
    if selection == "y":
        main_menu()
    elif selection == "n":
        exit()
    else:
        print("Wrong selection! Try again!")
        another_conversion()

# exit the code
def exit():
    print("Bye!!!")

# call the code main_menu()
def main():
    main_menu()

main()

