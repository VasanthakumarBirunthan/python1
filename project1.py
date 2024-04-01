#mtho 1
score= 0
play_intrest=input("Do you want to play (yes or no) :  ")
play_intrestlowercase=play_intrest.lower()
if play_intrestlowercase=="yes": #why we didn't use(playintrst == yes) conditionn inside  the if conditional statement
    #what if user type yes as YES/ Yes  it results fault because of case sensitivity output shown here 
    #Do you want to play (yes or no) :  YES
  #ok Next Time  we will meet at here bye!
    
    # instead of len() function we use the lower() function to change the all leters to small letters 
    print("lets go ") 
    Question=input("unit of Heat energy ?  ") 
    if Question== "J "or Question=="j" :
        print("Correct  !!!")
        score+=1
    else:
        print("wrong")
    Question=input("what is RAM ?  ")     
    if  Question=="random access memory" :
        print("Correct  !!!")
        score+=1
    else:
        print("wrong")
    Question=input("what is ipl stands for  ?  ")    
    if Question=="indian premier league" :
        print("Correct  !!!")
        score+=1
    else:
        print("wrong")     
    Question=input("what is the abbreviation of ICC ?  ")    
    if Question=="international cricket council" :
        print("Correct  !!!")
        score+=1
    else:
        print("wrong") 
    print(f"you got {score} out of 4")            





else:
    print("ok Next Time  we will meet at here bye! ")  







"""
play_intrest=input("Do you want to play (yes or no) :  ")
if len(play_intrest)> 2 : #why we didn't use(playintrst == yes) conditionn inside  the if conditional statement
    #what if user type yes as YES/ Yes  it results fault because of case sensitivity output shown here 
    #Do you want to play (yes or no) :  YES
  #ok Next Time  we will meet at here bye!
    #here u got a prob what if user mistakenly enters something as noo this will guide user to  play a game so
    #that we use method 1
    
    # instead of len() function we use the lower() function to change the all leters to small letters 
    print("lets go ")




else:
    print("ok Next Time  we will meet at here bye! ")    """
