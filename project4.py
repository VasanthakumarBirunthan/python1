"""
locate_row=int(input(('enter row where u want to place X ')))
locate_column=int(input(('enter column where u want to place X ')))
list1=[["arun","abi","asin"],["biru","bertu","bashir"]]
order=list1[locate_row][locate_column]

print(f'passed to the {order}')

row_1=['*','*','*']
row_2=['*','*','*']
row_3=['*','*','*']


guessedword=input('enter the 3 letter word that u guessed:  ')
player2guesed=[]
guessedletter =input('enter the letter:  ')

while len(player2guesed)!=3:
    if guessedletter in guessedword :
       print("nice you got one right")
       player2guesed.append(guessedletter)
    else:
     print('you lost one chance')   
    
    guessedletter =input('enter the letter:  ')
    if  guessedletter in guessedword   :
      print("nice you got 2nd right")
      player2guesed.append(guessedletter)
    else:
      print('you lost one chance') 
    guessedletter =input('enter the letter:  ')    
    if  guessedletter in guessedword   :
        print("nice you got 4th right")
        player2guesed.append(guessedletter)  
    else:
       print('you lost one chance') 
    guessedletter =input('enter the letter:  ')
    if  guessedletter in guessedword   :
        print("nice you got 5th right")
        player2guesed.append(guessedletter)
    else:
       print('you lost one chance') 
    guessedletter =input('enter the letter:  ')
    if  guessedletter in guessedword   :
        print("nice you got 6th right")
        player2guesed.append(guessedletter)
    else:
      print('you lost lst chance') 
   





print(player2guesed)    """
guessedword=input('enter the 3 letter word that u guessed:  ')
player2guesed=[]
count=0
while  len(player2guesed) < len(guessedword) and count<6 :

    guessedletter =input('enter the letter:  ')
    count+=1
    if guessedletter in guessedword:
        player2guesed.append(guessedletter)
        
    else:
        print('lost o n e')    
print(player2guesed)
print(count)
if len(player2guesed)==3  :
    print('you find it before the hangmen death')
else:
    print('sad to say better luck nxt time')


