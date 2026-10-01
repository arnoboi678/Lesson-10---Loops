for i in range (4, 43, 5):
    print(i)
n = int(input("Enter the amount whose sum you want to find"))
sum = 0
for i in range (n+1):
    sum = sum+i
print("sum =", sum)