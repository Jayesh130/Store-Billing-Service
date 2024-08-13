#importing modules to access the required function
import purchase
import sell
import view



print("\n") 
print("\n")
print("                                                      Jayesh Electronics                                                                              ")
print("\n")
print("                                        Baneshwor,Kathmandu | Phone No: 9818575447                                                                    ")
print("\n")

print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                    Welcome to the system ! I hope you have a good day ahead!                                                         ")
print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("\n")
def main():
    """This fuction call different function from different modules according to input"""
    while True:
        try:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Given below are some of the options for you to carryout the needed operations in the system")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("(1)  Press 1 to Sell the laptop to costumer.")
            print("(2)  Press 2 to Purchase from manufacturer.")
            print("(3)  Press 3 to Exit.")
            option=int(input("Enter an option: "))
            if option==1:
                '''When 1 is selected for Sale the laptop to costumer.'''
                sell.sell_() 
                
            elif option==2:
                '''When 2 is selected user Purchase from manufacturer.'''
                purchase.purchase_() 

            elif option==3:
                '''If selected option is equal to 3 the program should terminate. '''
                print("\tThank you for using the system, have a good day!")
                exit() 
            else:
                print("Does not seem to match as per our requirement. Please look at the option and try again.")
            print("\n"*2)
            
        except ValueError:
            print("Please look at the option and try again.")
            
#main function is called
main()


