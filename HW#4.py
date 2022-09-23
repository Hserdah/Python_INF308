




def main():
    #shelf and cart, cart being empty
    Shelf = ["bread","apple","jam","Chicken"]
    Cart = []
    
    print("welcome to the store check out what we have on the shelf",Shelf)
    
    #while loops until the list is empty
    while(Shelf.__len__() > 0):
        print("what items do you want to purchase?")
        print("when done please type checkout")
        x = input()
        #test to see in shelf and removes the item in shelf
        if(x in Shelf):
            Cart.append(x)
            Shelf.remove(x)
            #quits when user is done
        elif(x.lower() == "checkout"):
            print("thank you for shopping here your cart",Cart)
            ex()
            #make sures the stuff they take is actually in a list
        else:
            print("sorry the item you requested is out of stock")
    #if they empty the list they go here and quits        
    print("wow you must be rich you bought the entire store thank you for shopping")
    ex()
    
    
    
#quit function
def ex():
    quit()



main()