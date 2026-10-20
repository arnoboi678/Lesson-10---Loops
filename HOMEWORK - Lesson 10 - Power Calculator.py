base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent number: "))
result = 1
for i in range(exponent):
    result = result * base
print(result)