import sys


try:
    # let the user input a nbr
    integer = input("Enter a number : ")
    def collatz(integer):
        # if number is even then divide by 2
        if integer % 2 == 0:
            integer = integer / 2
            #can also print like below without converting it inot str 
            print("%s" % (integer))
        # if nbr is odd then multiply by 3 and add 1
        else:
            integer = 3 * integer + 1
            print(str(integer))
        return integer


    # keep doing the above caculations until the input value reduces to 1!
    while int(integer) > 1:
        integer = collatz(int(integer))
    else:
        exit(0)

except ValueError as err:
    print("error : {0}".format(err))
    sys.exit()









