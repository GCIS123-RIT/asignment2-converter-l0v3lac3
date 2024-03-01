"""
Group Member Names and Contributions:

Yara Hasan Alhourani: Wrote code for all the functions to convert from AED to other currencies. [aed_to_euro(money), aed_to_british_pound(money), aed_to_dollar(money)]
Wubrist Zewdie: Wrote code for all the functions to convert from Other currencies to AED. [euro_to_aed(amount), british_pound_to_aed(amount), dollar_to_aed(amount), others_to_aed()]
Afifa Monzur: Wrote code for the main menu, and submenus and remaining functions. [main_menu(), another_conversion(), exit(), aed_to_others()]

This program converts currencies from AED to EUR, GBP, USD and vice versa.

"""
euro_rate = 0.2513 # Rate of Euro 
pound_rate = 0.2151 # Rate of British Pound
dollar_rate = 0.2723 # Rate of USD

# This converts the amount from AED to Euro.
def aed_to_euro(money):
    """
    Converts the user input from AED to Euros.
    Parameter: money, float value, amount in AED.
    Returns amount in Euros.
    """
    euro = euro_rate * money
    print(money, "AED is equal to", euro, "EUR") 

# This converts the amount from AED to Pound
def aed_to_british_pound(money):
    """
    Converts the user input from AED to pound.
    Parameter: money, float value, amount in AED.
    Returns amount in Pound.
    """
    pound=pound_rate * money
    print(money, "AED is equal to", pound, "GDP")

# This converts the amount from AED to Dollar 
def aed_to_dollar(money):
    """
    Converts the user input from AED to dollar.
    Parameter: money, float value, amount in AED.
    Returns amount in dollar.
    """
    dollar=dollar_rate * money
    print(money, "AED is equal to", dollar, "USD")

# This converts the amount from Euro to AED 
def euro_to_aed(amount):
    """
    Converts the user input from Euro to AED.
    Parameter: money, float value, amount in Euro.
    Returns amount in AED.
    """
    aed = amount / euro_rate 
    print(amount, "GDP is equal to", aed, "AED")

# This converts the amount from pound to AED
def british_pound_to_aed(amount):
    """
    Converts the user input from pound to AED.
    Parameter: money, float value, amount in pound.
    Returns amount in AED.
    """
    aed= amount / pound_rate
    print(amount, "GDP is equal to", aed, "AED")

# This converts the amount from dollar to AED
def dollar_to_aed(amount):
    """
    Converts the user input from dollar to AED.
    Parameter: money, float value, amount in dollar.
    Returns amount in AED.
    """
    aed= amount / dollar_rate 
    print(amount, "USD is equal to", aed, "AED")

# convert submenu aed to other currency
def aed_to_others():
    try:
        money = float(input("Enter the amount you want to convert: "))
        if money < 0: # Makes sure that money amount is positive
            print("Invalid amount, try again!")   
            aed_to_others()
    except:
        print("Invalid amount, try agin!")   
        aed_to_others()

    print("\n 1. AED to Euro (EUR) \n 2. AED to British Pound (GBP) \n 3. AED to US Dollar (USD) \n")
    aed_to_other_selection = int(input("Enter the target currency from the above menu: "))
    while True:
        try:
            if aed_to_other_selection == 1:
                aed_to_euro(money)
                another_conversion()
                break
            if aed_to_other_selection == 2:
                aed_to_british_pound(money)
                another_conversion()
                break
            if aed_to_other_selection == 3:
                aed_to_dollar(money)
                another_conversion()
                break
        except:
            print("Error! Try again")
            aed_to_others()

# converts from other currency to AED
def others_to_aed():
    amount = float(input("Enter the amount you want to convert: "))
    if amount < 0:
        print("Invalid amount")   
        others_to_aed()
    print("\n 1. Euro (EUR) to AED \n 2. British Pound (GBP) to AED \n 3. US Dollar (USD) to AED \n")
    aed_to_other_selection = int(input("Enter the target currency from the above menu: "))
    while True:
        try:
            if aed_to_other_selection == 1:
                euro_to_aed(amount)
                another_conversion()
            if aed_to_other_selection == 2:
                british_pound_to_aed(amount)
                another_conversion()
            if aed_to_other_selection == 3:
                dollar_to_aed(amount)
                another_conversion()
        except:
            print("Error! Try again")
            continue

# Display the main menu
def main_menu():
    while True:
        print("------------------------------")
        print("\t\"Main Menu\"")
        print("Welcome to Currency Converter")
        print("------------------------------")
        print("\n 1. AED to other currencies \n 2. Other currencies to AED. \n 3. Exit \n")
        menu_selection = int(input("Enter the conversion direction - Choice(1/2/3): "))
        if menu_selection == 1:
            aed_to_others()
            break
        if menu_selection == 2:
            others_to_aed()
            break
        if menu_selection == 3:
            print("Bye!!!")
            break        
        else:
            print("Invalid choice! Try again!")
            continue

# If user wants to convert again
def another_conversion():
    while True:
        selection = input("Do you want to do another conversion? (y/n): ")
        if selection == "n" or "N":
            exit()
            break
        elif selection == "y" or "Y":
            main_menu()
            break
        else:
            print("Wrong selection! Try again!")
            another_conversion()

# Exits the code
def exit():
    print("Bye!!!")


def main():
    main_menu()

if __name__ == "__main__":
    main() # call the function main_menu()

