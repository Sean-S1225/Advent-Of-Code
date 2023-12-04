arr = []
totalSum = 0

with open("./Data.txt", "r") as data:
    for line in data:
        arr.append(line)

for x in arr:
    num1, num2 = 0, 0
    for y in x:
        if y.isdigit():
            num1 = y
            break
    for y in x[::-1]:
        if y.isdigit():
            num2 = y
            break
    
    totalSum += int(num1 + num2)

print(totalSum)