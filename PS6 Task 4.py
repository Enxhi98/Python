def shoplist():
        quitshop = False
        shoppinglist = []

        while (quitshop == False):
            print (" ")
            print("This is your shopping list ")
            print (" ")
            for item in shoppinglist:
                print(item)
                

            print (" ")
            print ("Menu")
            print (" ")
            print ("1 = Add item")
            print ("2 = Add multiple items to list")
            print ("3 = Your list")
            print ("4 = Sort into alphabetical order")
            print ("5 = Quit")
            userchoice = int(input ("Please enter the option you want to proceed with "))

            if (userchoice == 2):
                print("You chose option 2")
                
                additem = "add"
    
                while additem != "":
                    additem = input ("Please enter item for list: ")

                    if additem != "" and "additem":
                        shoppinglist.append(additem)
                    
            elif (userchoice == 1):
                additem = input ("Please enter an item you want to add: ")
                shoppinglist.append(additem)
                
            elif (userchoice == 3):
                print("Your list contains:", shoppinglist)
                
            elif (userchoice == 4):
                print("This is sorted")
                shoppinglist.sort()
                
            elif (userchoice == 5):
                print("You have chosen to quit the program")
                quit
                quitshop = True
                 
            else:
                print ("error")
                print ("Try again")

if __name__== "__main__":
    shoplist()
