x = "abc" +"4"
#print(x)
print(type("4"))
x = 5

if not x == 5:
    print("x is not equal to 10")

marks=67

if marks > 75:
    print('A')

if 60 <= marks < 75:
    print('B')

elif 40 <= marks < 60:
    print("C")

else:
    print( 'F')
tuple5 =(4,6,780)
print(tuple5)
print(tuple5[1])

#for num in range(1,5) :
height=input("Enter heights in cm with space: ")
height_lst=height.split()
print(height_lst)
tot=0
for heights in height_lst:
  tot += int(heights)
avg=tot/len(height_lst)
print(avg ) 


res=int(input(''))
tsum=0
for i in range(res):
    sum=int(input(""))
    tsum=tsum+sum
print(tsum)
