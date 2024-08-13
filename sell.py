#importing required modules and functions
import datetime
import validateID
import view
   
def validate_quanitiy(data,sno):
    '''this function takes dictionary and sno as parametrs to verify quantity'''
    continueloop =True
    while continueloop==True:
        try:
            quantity=int(input("Enter Number of laptop you want to purchase: "))
            if quantity>0 and quantity <=int(data[sno][3]):
                print("The quantity is available")
            
                return quantity
                continueloop=False

            else:
                print("The quantity is unavailable.Please re-enter the value\n")
                view.display_laptop(data)
        except ValueError:
            print("Please enter numeric value")
            
def invoice_gen(lists_sell):
    """It takes list that consists of SNO and quantity to generate a invoice and display and write it"""
    brand_sell=[]    # creating empty list to add the brand of laptop that was purchased
    name_sell=[]    # creating empty list to add the name of laptop that was purchased
    total=0     
    time=datetime.datetime.now()   #storing current date and time
    content=view.get_content()
    data=view.dictionary_laptop(content)    #calling dictionary_laptop(content)
    shipping_cost = 100
    username=input("Enter your name : ")
    num=input("Enter your number : ")
                                            
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t"*5,"Invoice")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name : "+username)
    print("Conatct : "+num)
    print("Time : "+ str(time))
    print()
    print("ID","\t","Laptop Name","\t\t"," Brand","\t","Quantity","\t","Price")
    print("")
    
    for i in range(len(lists_sell)):
        sno1=int(lists_sell[i][0])
        qauntity1=int(lists_sell[i][1])
        LaptopName=data[sno1][0]
        name_sell.append(LaptopName)
        LaptopBrand=data[sno1][1]
        brand_sell.append(LaptopBrand)
        qty=int(data[sno1][2].replace("$",""))
        price=qauntity1*qty
        total +=price
        print(str(sno1),"\t",LaptopName,"\t",LaptopBrand,"\t","  ",str(qauntity1),"\t\t","$",str(price))
        print("\n")
    print("Price :      "+"$"+str(total))
    print("\n")
    print("Shipping:    "+"$"+str(shipping_cost))
    print("\n")
    print("Total Price: "+"$"+str(total + shipping_cost))
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                          THANK YOU FOR PURCHASING THE LAPTOP                                                                    ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
     
    billnumber=num
    bill=open(billnumber+".txt","w")
    bill.write("\n")
    bill.write("\n") 
    bill.write("                                                      Jayesh Electronics                                                                        ")
    bill.write("\n")
    bill.write("                                        Baneshwor,Kathmandu | Phone No: 9818575447                                                             ")
    bill.write("\n")

    bill.write("--------------------------------------------------------------------------------------------------------------------------------------------------")
    bill.write("                                          THANK YOU FOR PURCHASING THE LAPTOP                                                                    ")
    bill.write("--------------------------------------------------------------------------------------------------------------------------------------------------")
    bill.write ("\n")
    bill.write("-------------------------------------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    bill.write("                                                   Invoice                                                                                      ")
    bill.write("\n")
    bill.write("-------------------------------------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    bill.write("Name : "+username)
    bill.write("\n")
    bill.write("Conatct : "+num)
    bill.write("\n")
    bill.write("Time : "+ str(time))
    bill.write("\n")
    bill.write("\n")
    bill.write("ID"+"\t"+"Laptop Name"+"\t"+" Brand"+"\t"+"Quantity"+"\t"+"Price")
    bill.write("\n")
    bill.write("\n")
    
    for i in range(len(lists_sell)):
        sno1=int(lists_sell[i][0])
        qauntity1=int(lists_sell[i][1])
        LaptopName=data[sno1][0]
        name_sell.append(LaptopName)
        LaptopBrand=data[sno1][1]
        brand_sell.append(LaptopBrand)
        qty=int(data[sno1][2].replace("$",""))
        price=qauntity1*qty
        bill.write(str(sno1)+"\t"+LaptopName+"\t"+LaptopBrand+"\t"+"  "+str(qauntity1)+"\t\t"+"$"+str(price))
        bill.write("\n")
        bill.write("\n")
        
    bill.write("Price :      "+"$"+str(total))
    bill.write("\n")
    bill.write("Shipping:    "+"$"+str(shipping_cost))
    bill.write("\n")
    bill.write("Total Price: "+"$"+str(total + shipping_cost))
    bill.write("\n")
    bill.write("-------------------------------------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    
   
    bill.write("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    bill.close()
            
def overwrite_file(data):
    '''the fucntion overwrites stock.txt with new values'''
    file = open("stock.txt", "w")
    for value in data.values():
        new_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3])  + "," + str(value[4])+ "," + str(value[5]) + "\n"
        file.write(new_data)
    file.close()
   
def sell_():
    '''this function stores all the values returned by other functions'''
    lists_sell=[]
    content=view.get_content()
    data=view.dictionary_laptop(content)
    continueLoop = True
    while continueLoop == True:
        view.display_laptop(data)
        sno=validateID.validate_laptop_id(data)
        quantity=validate_quanitiy(data,sno)
        data[sno][3]=" "+str(int(data[sno][3])-quantity)
        lists_sell.append([sno,quantity])
        view.display_laptop(data)
        over_wite=overwrite_file(data)
        userInput = input("Do you want to order more laptops? yes/no ")
        if userInput.lower() == "no":
            continueLoop = False
        elif userInput.lower() == "yes":
            continueLoop = True
    invoice=invoice_gen(lists_sell)



