import random  #usually we import random module at the startimg of the programme becz if programmer  have to use random methods at that time 
# this action would be usefull
user_input=input("Enter rock/paper/scissor or u can quit the game with q : ").lower() #lower method same as typecasting we can use it at input linecode
""" user_input=input("Enter rock/paper/scissor or")
 user_inputlowercase=user_input.lower()
   """
choices=["rock","paper","scissor" ] 

while True:
    if user_input == "q" :
        quit()  
    if user_input not in choices      : # why we didn't use elif in here if we use it ,,if this statement evaluate true 
        #if there is anymore elifs foolowing 1st elif they are skiiped because of this so that we use IF in here
        print("can you enter valid input strike")
    
        continue

        

