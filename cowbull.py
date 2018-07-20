import random
game_counter=0
computer_input=0
def generator():
    while(True):
        global computer_input
        computer_input=str(random.randint(1000,9999))
        x=0
        for i in range(0,4):
            x=x+computer_input.count(computer_input[i])
        if(x==4):
            break
generator()
#print(computer_input)
bull_count=0
cow_count=0
while(True):
    print("Input your number to know the number's comparision with the generated number")
    while(True):
        try:
            player_input=int(input("Enter Your Number:"))
        except ValueError:
            print("The string you entered is not a number")
            break
        player_input=str(player_input)    
        if len(player_input)==4:
            for i in range(0,4):
                for j in range(0,4):
                    if(i==j)and(computer_input[i]==player_input[j]):
                        bull_count+=1
                    elif(i!=j)and(computer_input[i]==player_input[j]):
                        cow_count+=1
                    else:
                        pass
        else:
            print("the number you entered is not a 4 digit number")
            break                
        game_counter+=1            
        if(bull_count!=4):
            print("cow_count is:",cow_count)
            print("bull_count is:",bull_count)
        else:
            print("you guessed the correct number in "+str(game_counter)+" chances" ) 
            print("do you want to play again")
            opt=input("Enter \"yes\" or \"y\" to play again. Or anything else to exit:")
            if opt=="yes" or opt=="y":
                generator()
            else:
                exit()    
        cow_count=0
        bull_count=0
        
    

            