
def print_pyramid(n):
    #first for loop the upper half of the hourglass 
    for i in range(n+1):
        symb = '* '* (n-i)
        space = ' '*(i)
        if symb !='':
            print (space+symb)

    #first for loop the lower half of the hourglass 
    for i in range(2, n+1):
        symb = '* '*(abs(i))
        space = ' '*(n-i)
        if symb !='':
            print (space+symb)


if __name__ == "__main__":
    # input from the user
    print_pyramid(input("N= "))