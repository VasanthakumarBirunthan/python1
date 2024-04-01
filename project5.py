name_1=input('enter your name1: ' )
name_2=input("enter your  partner's name:  ")
combinedname=name_1+name_2

com_namelowered=combinedname.lower()# .lowermethod is used to all letters to lowercase especially in strings
t=com_namelowered.count('t')
r=com_namelowered.count('r')
u=com_namelowered.count('u')
e=com_namelowered.count('e')


l=com_namelowered.count('l')
o=com_namelowered.count('o')
v=com_namelowered.count('v')
e=com_namelowered.count('e')
sum1=t+u+e+r
sum2=l+o+v+e
tot=int(str(sum1)+str(sum2))


#print("your True love percentage is, tot, %")


print(f"your True love percentage is {tot} %")
"""if int(tot )> 90 : #in this line i used to typecast becz (TypeError: '>' not supported between instances of 'str' and 'int'
    print('bestuu')
elif 10<int(tot)<90:
    print('nice pair get in deeper')
else:
    print('more to find')   
"""
if tot > 90 : #in this line i used to typecast becz (TypeError: '>' not supported between instances of 'str' and 'int'
    print('bestuu')
elif 10<tot<90:
    print('nice pair get in deeper')
else:
    print('more to find')
