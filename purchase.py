#importing required files and functions
import datetime
import validateID
import view

def laptopID_validate(data):
    while True:
        try:
            ID = int(input("Enter S.No of the laptop you want to order: "))
            if ID > 0 and ID <= len(data):
                print("\n__________________________________________________________________________________________________________________________________")
                print("                                                     The Laptop is available                                                        ")
                print("__________________________________________________________________________________________________________________________________\n")
                return ID
            else:
                print("Please enter laptop ID")
        except ValueError:
            print("Please enter numeric value")

def validate_quanitiy(data,sno):
    """It takes dictionary and SNO as parameter and verifies the quantity on the basis of that"""
    continueloop =True
    while continueloop==True:
        try:
            quantity=int(input("Enter Number of laptop you want to order: "))
            if quantity>0 :
                print("Thank you for ordering the laptop")
            
                return quantity
                continueloop=False
            else:
                print("Please enter valid quantity\n")
                view.display_laptop(data)
        except ValueError:
            print("Please enter numeric value")
            
def invoice_gen(lists_purchase):
    """It takes list that consists of SNO and quantity to generate a invoice and display and write it"""
    brand_purchase=[]    # creating empty list to add the brand of laptop that was sold
    name_purchase=[] # creating empty list to add the brand of laptop that was purchased
    total=0
    time=datetime.datetime.now()    #storing current date and time 
    content=view.get_content()
    data=view.dictionary_laptop(content)     #calling dictionary_dress(content) from view.py and storing it
    name = input("Enter your name :")
    number = input("Enter your number :")
    print()
    print("________________________________________________________________________________________________________________________________________________")
    print("\t"*5,"PURCHASE INVOICE")
    print("________________________________________________________________________________________________________________________________________________")
    print("Name : "+name)
    print("Conatct : "+number)
    print("Time : "+ str(time))
    print()
    print("ID","\t","Laptop Name","\t\t"," Brand","\t","Quantity","\t","Price")
    print("")
    for i in range(len(lists_purchase)):
        sno1=int(lists_purchase[i][0])
        qauntity1=int(lists_purchase[i][1])
        LaptopName=data[sno1][0]
        name_purchase.append(LaptopName)
        LaptopBrand=data[sno1][1]
        brand_purchase.append(LaptopBrand)
        qty=int(data[sno1][2].replace("$",""))
        price=qauntity1*qty
        total +=price
        print(str(sno1),"\t",LaptopName,"\t",LaptopBrand,"\t","  ",str(qauntity1),"\t","$",str(price))
        print("\n")
    print("Price (without VAT): "+"$"+str(total))
    print("\n")
    print("VAT: "+"$"+str(total*0.13))
    print("\n")
    print("Price   (with VAT) :"+"$"+str(total * 1.13))
    print("________________________________________________________________________________________________________________________________________________")

    billnumber=number
    bill=open(billnumber+".txt","w")  #creates new file on the basis of phone number and overwrites it
    bill.write("\n")
    bill.write("___________________________________________________________________________________________________________________________________________")
    bill.write("\n")
    bill.write("\t\t\t\t\t"+"PURCHASE INVOICE ")
    bill.write("\n")
    bill.write("___________________________________________________________________________________________________________________________________________")
    bill.write("\n")
    bill.write("Name : "+name)
    bill.write("\n")
    bill.write("Conatct : "+number)
    bill.write("\n")
    bill.write("Time : "+ str(time))
    bill.write("\n")
    bill.write("\n")
    bill.write("ID"+"\t"+"Laptop Name"+"\t"+" Brand"+"\t"+"Quantity"+"\t"+"Price(per)")
    bill.write("\n")
    bill.write("\n")
    
    for i in range(len(lists_purchase)):
        sno1=int(lists_purchase[i][0])
        qauntity1=int(lists_purchase[i][1])
        LaptopName=data[sno1][0]
        name_purchase.append(LaptopName)
        LaptopBrand=data[sno1][1]
        brand_purchase.append(LaptopBrand)
        qty=int(data[sno1][2].replace("$",""))
        price=qauntity1*qty
        bill.write(str(sno1)+"\t"+LaptopName+"\t"+LaptopBrand+"\t"+"  "+str(qauntity1)+"\t"+"$"+str(price))
        bill.write("\n")
        bill.write("\n")
 
    bill.write("Price (without VAT): "+"$"+str(total))
    bill.write("\n")
    bill.write("VAT: "+"$"+str(total*0.13))
    bill.write("\n")
    bill.write("Price   (with VAT) :"+"$"+str(total * 1.13))
    print("________________________________________________________________________________________________________________________________________________")
    
    bill.close()
            
def overwrite_file(data):
    """It takes the final dictionay and overwites stock.txt with new values"""
    file = open("stock.txt", "w")
    for value in data.values():
        new_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3])  + "," + str(value[4])+ "," + str(value[5])+ "\n"
        file.write(new_data)
    file.close()
    
def purchase_():
    """It stores all the values returned by other functions """
    lists_purchase=[]
    content=view.get_content()
    data=view.dictionary_laptop(content)
    continueLoop = True
    while continueLoop == True:
        view.display_laptop(data)
        sno= laptopID_validate(data)
        quantity=validate_quanitiy(data,sno)
        data[sno][3]=" "+str(int(data[sno][3])+quantity)    #updating quantity on dictionary
        lists_purchase.append([sno,quantity])
        view.display_laptop(data)
        over_wite=overwrite_file(data)
        userInput = input("Do you want to order more laptops? yes/no ") #asking user if they want to return more laptop
        if userInput.lower() == "no":
            continueLoop = False
    invoice=invoice_gen(lists_purchase)
 

