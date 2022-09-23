


def main():
    #loops until you go to ex funct
    while(1):
        print("how much money do you make")
        money = float(input())
        try:
            float(money)
        except:
             print("This is not a number")
             main()
        #if it is zero restarts and does not go through the rest of the program
        if(money <= 0):
            print("your income is 0 you have no taxes")
            main()
        y = taxes(money)
        print("here is you money after taxes", '{0:.2f}'.format(y))
        print("would you like to do this again?")
        answer = input()
        #if no regardless of capitals will end program
        if(answer.lower() == "no"):
            ex()
        
        

# does the calculations based on income
def taxes(money):

    if(money <= 10000):
        return(money)
    elif(money > 10000 and money <= 50000):
        aftertaxes = money * .2
        return(money - aftertaxes)
    elif(money > 50000 and money <= 75000):
        aftertaxes = money * .35
        return(money - aftertaxes)
    elif(money > 75000):
        aftertaxes = money * .5
        return(money - aftertaxes)

#quits program
def ex():
    print("have a nice day")
    quit()



main()
