
def main():
    #The dictionary and list the tuple is later
    dict = {}
    arr = []
   
    while(1):
        print("hello what is your name?")
        name = input()
        #add the name
        arr.append(name)
        print("what is your eye color?")
        eye = input()
        #make tuple add eye color
        tup = (eye)
        print("where do you live?")
        add = input()
        print("Zip code?")
        zip = input()
        #add the address and zip
        dict[add] = zip
        print("here is your recorded info")
        print(arr,tup,dict)
        print("would you like to do this again?")
        answer = input()
        #if no regardless of capitals will end program
        if(answer.lower() == "no"):
           
            ex()
        
#exit function   
def ex():
    print("have a nice day")
    quit()



main()