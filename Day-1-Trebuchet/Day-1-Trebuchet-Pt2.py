arr = []
totalSum = 0

def ContainsNum(s):
    numeric = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    allowed = numeric + words
    
    for a in allowed:
        if a in s:
            if a in numeric:
                return a
            else:
                return dict(zip(words, numeric))[a]
    return False

with open("./Data.txt", "r") as data:
    for line in data:
        arr.append(line)

for x in arr:
    num1, num2 = 0, 0
    
    for y in range(0, len(x)):
        if (z := ContainsNum(x[:y])):
            num1 = z
            break

    for y in range(1, len(x)+1):
        if (z := ContainsNum(x[-y::])):
            num2 = z
            break

    totalSum += int(num1 + num2)

print(totalSum)