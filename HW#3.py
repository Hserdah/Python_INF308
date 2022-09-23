def main():
    file = open('text.txt', 'w')
    #while loop to keep the adding more address
    while(1):
        print("hello to your personal online address book!")

        print("first please input the mname of the person ")

        s = input()

        file.write(s + "\n")

        print("next please input the address of the person")

        x = input()

        file.write(x + "\n")

        print("anyone else?")

        answer = input()
        # if no regardless of capitals will end program
        if(answer.lower() == "no"):
            file.close()

            file = open('text.txt', 'r')

            print(file.read())

            file.close()
            ex()

#quit function
def ex():
    quit()


main()
