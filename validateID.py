"""Laptop ID should be validate on both purchase and sell
so, Id validation is done in another fie"""
def validate_laptop_id(data):
    '''creating validate_laptop_id(data) function which takes dictionary as parameter and validates laptop ID'''
    while True:
        try:    #Exception handeling
            sno=int(input("Enter S.No of the laptop you want to purchase: "))
            if sno > 0 and sno <= len(data):
                return sno
            else:
                print("Please enter available S.No")
        except ValueError:
            print("Please enter numeric value")
