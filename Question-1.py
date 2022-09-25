##Write a Python Program to Find the Factorial of a Number?

num=int(input("Enter a number whose factorial need to be checked: "))
fact=1
if num<0:
        print("Enter a positive integer only")
elif num==0:
        fact=1
        print("The factorial of 0 is : 1")
else:
    for i in range(1, num + 1):
        fact=fact*i
    print("The factorial value",num,"is:",fact )


