
while True:
    age = int(input("Enter your age: "))
    if age > 0:
        break 
    print("Invalid input. Please enter a number greater than 0.")

s = age * (age + 1) // 2 
print("Expected sum is", s)

def getSum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("After calling the function getSum, the sum of all numbers from 1 to", age, "is:", getSum(age))

if getSum(age) == s:
    print("Output Verified.")
