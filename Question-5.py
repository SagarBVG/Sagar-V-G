##Write a Python Program to Find Armstrong Number in an Interval?

lower = int(input("Enter a lower limit: "))
upper = int(input("Enter a higher limit: "))

for num in range(lower, upper + 1):
    len_num= len(str(num))
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len_num
        temp //= 10

    if num == sum:
        print(num)