age=30
name="novoc"
print(" my name is " , name , '  i am'  ,age,)
tot=0
for num_1 in range(0,101,2) :
    tot=tot+num_1 
print(tot)    
count_1=0
total_1=0
while count_1  < 101 :
    total_1+= count_1
    count_1+=2
print(total_1)
total_2=0
for num_2 in range(2,101):
    if num_2%2==0:
        total_2+=num_2
    else:
        pass
print(total_2)    
for i in range(0,100):
    if i%3==0:
        print('fizz')
        if i%5==0:    
           print('fizzbuzz')
    elif i%5==0:
        print('buzz')


    else: 
     print(i)   
"""
price=0

if input("do u want ch2eese")=="yes ":
    price+=20
if input(" enter ur pizza size")  == "small" :
    price+=100
    if input("do u want poporoni")== "yes" :
        price+=50
    
elif input(" enter ur pizza size") =="medium" :
    price+=200
    if input("do u want poporoni")== "yes" :
        price+=80

elif input(" enter ur pizza size")  =="large" :
    price+=300
    if input("do u want poporoni") == "yes" :
        price+=80

print(price)"""
"""" price=0
size=input(" what  siz Do u want :   ")



if size== "small":
    price+=100
elif size=="medium " :
    price+=150
elif size=="large" :
    price+=300
popin=input("Do u want extra popin:   ")   
if popin=="yes" :
    if size=="small" or size=="medium ":
        price+=60
    else:
        price+=50
else:
    pass  
    
 cheese=input("Do u want extra cheese:   ")
if   cheese=="yes"        :
    price+=20
else:
    pass    """
print(price)"""


price = 0
size = input("What size do you want: ")

if size == "small":
    price += 100
elif size == "medium":
    price += 150
elif size == "large":
    price += 300

popin = input("Do you want extra popin: ")

if popin == "yes":
    if size == "small" or size == "medium":
        price += 60
    else:
        price += 50

cheese = input("Do you want extra cheese: ")

if cheese == "yes":
    price += 20

print("Total price:", price)


