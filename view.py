def get_content():
    '''reads items present in the txt file'''
    storage=open("stock.txt","r")
    file=storage.read()
    file=file.split("\n")
    
    while(""in file):
        file.remove("")
    return file

def dictionary_laptop(content):
    """It takes the stock file as parameter and puts it in a dictionary using keys and values"""
    laptop={}    #creating empty dictionary
    counter=0
    for i in range(len(content)):
        counter=counter+1   #using counter as key for dictionary
        laptop[counter]=content[i].split(",")
    return laptop

def display_laptop(data):
    '''print dictionary in tabular format'''
    #display dictionary in tabular format
    print("S.No.","\t","Laptop Name","\t\t"," Brand","\t","  Price","\t","Quantity","\t","Processor","\t","Graphics Card")
    for key,value in data.items():
        print(key,"\t",value[0].ljust(15),"\t",value[1].ljust(10),"\t",value[2].rjust(6),"\t",value[3],"\t\t",value[4],"\t",value[5])
        
def view_laptop():
    '''stores all the values returned by the function'''
    content=get_content()
    data=dictionary_laptop(content)
    display_laptop(data)

 
        
