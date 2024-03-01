"""
Group Member Names and Contributions:

Yara Hasan Alhourani: Wrote code for 
Wubrist Zewdie: Wrote code for  
Afifa Monzur: Wrote code for 

This 
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
    print("your exchange in euro:", euro)


def aed_to_british_pound(money):
    pound=pound_rate * money
    print("your exchange in pound:",pound)

def aed_to_dollar(money):
    dollar=dollar_rate * money
    print("your exchange in dollar:",dollar)

def euro_to_aed(amount):
    aed=amount/euro_rate 
    print("your exchange in dhm:",aed)

def british_pound_to_aed(amount):
    aed=amount/pound_rate
    print("your exchange in dhm:",aed)

def dollar_to_aed(amount):
    aed=amount/dollar_rate 
    print("your exchange in dhm:",aed)

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

def others_to_aed():
    amount = float(input("Enter the amount you want to convert: "))

def main_menu():
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

def another_conversion():
    selection = input("Do you want to do another conversion? (y/n): ")
    if selection == "y":
        main_menu()
    elif selection == "n":
        exit()
    else:
        print("Wrong selection! Try again!")
        another_conversion()

def exit():
    print("Bye!!!")


def main():
    main_menu()

main()
