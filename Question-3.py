##Write a Python Program to Print the Fibonacci sequence?

num = int(input("Enter a number of terms : "))

n1, n2 = 0, 1
i = 0

if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,"is :")
   print(n1)
else:
   print("Fibonacci sequence upto",num,"is :")
   while i < num:
       print(n1)
       temp = n1 + n2
       n1 = n2
       n2 = temp
       i += 1