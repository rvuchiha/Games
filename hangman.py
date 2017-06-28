#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GauthamVelmurugan
#
# Created:     22-06-2017
# Copyright:   (c) GauthamVelmurugan 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import sys
    a=['c','o','m','p','u','t','e','r']
    c=['','','','','','','','']
    k=0
    j=0
    print"Let's Play Hangman .........!!!!!"
    print"Total letter eight"
    print"__ __ __ __ __ __ __ __"
    print"Total 10 chances ............So let's Begin...."
    for k in range(10):
        if(a==c):
            print"Good the answer is :",c
            print"You Won"
            print"Bye"
            exit()
        elif(a<>c):
            b=str(raw_input("Guess a character"))
            if b in a:
                for i in range(8):
                    if(b==a[i]):
                        c[i]=a[i]
                        k+=1
                    else:
                        sys.stdout.write("")
        print c
    print "Game Over .......!!!"
    print"Your lost..."
    print"Try again later"
    print"Bye..."




if __name__ == '__main__':
    main()
