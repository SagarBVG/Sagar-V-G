##Write a Python Program to Display the multiplication Table?

num=int(input("Enter a number whose multiplication table need to be printed: "))
print("multiplication table of",num,"is as follows ")
for i in range(1,11):
    print(num, 'x', i, '=', num * i)