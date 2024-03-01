rate1=0.25
rate2=0.22
rate3=0.27


def aed_to_euro(money):
    euro=rate1*money
    print("your money in euro:",euro)
def aed_to_british_pound(money):
    pound=rate2*money
    print("your money in pound:",pound)
def aed_to_dollar(money):
    dollar=rate3*money
    print("your money in dollar:",dollar)
def euro_to_aed(money):
    aed=money/rate1
    print("your money in dirham:",aed)
def pound_to_aed(money):
    aed=money/rate2
    print("your money in dirham:",aed)
def dollar_to_aed(money):
    aed=money/rate3
    print("your money in dirham:",aed)
def from_aed_to_others(money):
    aed_to_euro(money)
    aed_to_british_pound(money)
    aed_to_dollar(money)
def from_others_to_aed(money):
    euro_to_aed(money)
    pound_to_aed(money)
    dollar_to_aed(money)
def main():
    money=int(input("amount of money for exchange="))
    conversion_direction=input("select direction 'to others'or'to aed':")
    while True:
     if money<0:
        print("error:you enter invalide amount of money")
        break
    #conversion_direction=input("select direction 'to others'or'to aed':")
     if conversion_direction=='to others':
       from_aed_to_others(money)
       break
     elif  conversion_direction=='to aed':
        from_others_to_aed(money)
        break
     else:
        print("you select invalid input for direction of conversion.please enter 'to others'or'to aed'")
main()