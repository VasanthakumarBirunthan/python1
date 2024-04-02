Guessed_num=input("Enter a number:  ")
if Guessed_num.isdigit():# returns True if socalled variable gueesednum str object is a digit
    #don't typecast input datatype in 1st line of code {str to int} because int objects doesn't support isdigit() method
    Guessed_num=int(Guessed_num)
    print(type (Guessed_num))
    if Guessed_num<0:
        print("Enter a num is greater than ZERO!!!!")
        quit()
    import random
    Random_num=random.randrange(0,10)
    
   


    if Random_num== Guessed_num :
        print("you got it !!!!!")
    else:
        print("next try []")    

        
else:
    print("Ensure that you are entering a number")    













        
        
      




















"""
num_2="90" #typeof num_2is a str
if num_2.isdigit(): #If the string contains only numeric characters (0-9), .isdigit() returns True
    print('num')


num_1=90     #typeof num_1is a int
if num_1.isdigit(): #AttributeError: 'int' object has no attribute 'isdigit'
    print('num')    
"""
