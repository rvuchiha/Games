#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      N.VINAY RAM
#
# Created:     23/06/2017
# Copyright:   (c) N.VINAY RAM 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import random
    lis="rock","paper","scissor"
    print 'choose ur option:',lis

    x=0
    y=0
    i=0
    while((x+y) <= 4 ):
            i+=1
            oup= random.choice(lis)
            inp=raw_input('Enter your choice :'+str(i)+'of 5 \n\trock \n\tpaper \n\tscissors\nTo exit:press any other key')
            if(oup==inp):
                print'the computer chose:',oup
                print'Its a draw'
            elif(inp==lis[0] and oup==lis[1]):
                x+=1
                print 'You Win\nyou:',x,'\nsystem:',y

            elif(inp==lis[0] and oup==lis[2]):
                y+=1
                print'System Wins\nyou:',x,'\nsystem:',y


            elif(inp==lis[1] and oup==lis[0]):
                x+=1
                print 'You Win\nyou:',x,'\nsystem:',y

            elif(inp==lis[1] and oup==lis[2]):
                y+=1
                print 'System Wins\nyou:',x,'\nsystem:',y

            elif(inp==lis[2] and oup==lis[0]):
                x+=1
                print 'You Win\nyou:',x,'\nsystem:',y

            elif(inp==lis[2] and oup==lis[1]):
                y+=1
                print 'System Wins\nyou:',x,'\nsystem:',y

            else:
                x=7
                exit
    if(x!=7):
        print 'You have \nwon',x,' \nlost',y,'\n\nTHANK YOU FOR PLAYING'
    else:
        print'You Have QUIT the Game'

if __name__ == '__main__':
    main()
