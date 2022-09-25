##Write a Python Program to Find the Sum of Natural Numbers?

num=int(input("Enter a number: "))
if num<0:
    print('Enter a positive number only')
else:
    sum = 0
    while(num>0):
        sum+=num
        num-=1
    print("The sum is: ",sum)