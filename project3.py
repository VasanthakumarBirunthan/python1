"""names=input('enter ur suggestions  by separated commas ;; ')
newname=names.split(' ,')#.split() method is used to separate the substring from string specifically we can seperate this with spceial delimiter within the  paranthesis
print(newname)

names1="abiselvaerodevpoeroni"
newname1=names1.split('e')#in here i used letter 'e' as a delimetre so that  i got the list as given below it starts separate the sub strings whenever face ''e''d

print(newname1)

players=input('type the all players name with the seperation of white space')
players_list=players.split(" ") #use double quoation dontuse single quotation otherwise list contain one value with separation of white space
import random            #if u want to use
winner=random.choice(players_list)
print('THE WINNER IS ' , winner ) #print(f'THE WINNER IS{ winner}' )
 






print(players_list)
print(players_list[1])"""


import random
specificnum=random.randrange(1,5)# randomly select a number within the range of 1 to 4 output will be 1/ 2 /3/ 4 but not 5
specificnum_randint=random.randint(1,5)# this will select anumber from the mentioned range also thiswill output 1 2  3 4 5



print(specificnum)
print(specificnum_randint)


players_45=input('type the all players name with the seperation of comma')
players_list45=players_45.split(" ") #use double quoation dontuse single quotation otherwise list contain one value with separation of white space
import random            #if u want to use module 1st importthen there wiill be an error as undefined
count=len(players_list45)
print(count)
winner=random.randint(0,count)
print(winner)
ogwin=players_list45[winner]
print(ogwin)
print(f'THE WINNER IS {ogwin} ' )




