import random  #usually we import random module at the startimg of the programme becz if programmer  have to use random methods at that time 
# this action would be usefull
#user_input=input("Enter rock/paper/scissor or u can quit the game with q : ").lower() #lower method same as typecasting we can use it at input linecode
# user_input=input("Enter rock/paper/scissor or")
 #user_inputlowercase=user_input.lower()
   
choices=["rock","paper","scissor" ] 
user_score=0
computer_score=0
while computer_score < 3 and user_score<3:
    user_input=input("Enter rock/paper/scissor or u can quit the game with q : ").lower()
    if user_input == "q" :
        quit()  
    if user_input not in choices      : # why we didn't use elif in here if we use it ,,if this statement evaluate true 
        #if there is anymore elifs folowing 1st elif they are skiiped because of this so that we use IF in here
        print("can you enter valid input strike")
        continue
    computer_strike=random.choice(choices)
    print(computer_strike)
    if user_input =="rock" and computer_strike=="scissor": 
        print("u win")  
        user_score+=1
    elif user_input =="scissor" and computer_strike=="paper": 
        print("u win")  
        user_score +=1
    elif user_input =="paper" and computer_strike=="scissor":
        print("u win")  
        user_score +=1    
    else:
        print("you lost")          
        computer_score+=1
print(f" user gets {user_score} wins")        
print(f" computer gets {computer_score} wins") 
print("hyu")  


