name=input("Ënter your name:  ")
print("welcome to the adventure",name,"Be Ready to face it")
challenge_1=input("there is a river in the route so what are u going to do swim or walk along the narrow bridge to cross if u want to walk to then enter walk?  ").lower()
if challenge_1=="swim":
    print("you can swim across the river to pass but take a look on crocodile and alligators!!!!!!")
    
    challenge_2=input("there is a cave in the route so what are u going to do jump or use the rope  to pass  if u want to use rope to then enter rope?  ").lower()
    if challenge_2=="jump":
        print("Nice move but u will lose more energy while in this procees!!!! ")
    elif challenge_2=="rope":
        print("so you chose to use rope then move forward  always have a look on your grip to avoid sliding!!!")
    else:
        print("There are no other ways at the moment")

elif challenge_1=="walk":
    print("so you chose to walk then move forward  You have to go farmiles to reach keep it in mind!!!")
    challenge_3=input("there is a hill in the route so what are u going to use motorcycle or ""jeep?"" to pass  if u want to use motorcycle then to  enter ""cycle""?  ").lower()
    if challenge_3=="jeep":
        print("you have to drive carefuuly with jeep take in control!!!!")
    elif challenge_3=="cycle":
        print("so you chose to use cycle  then move forward  always have a look on your path !!!")
    else:
        print("There are no other ways at the moment")


else:
    print("There are no other ways at the moment")