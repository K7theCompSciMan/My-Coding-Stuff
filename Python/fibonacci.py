num1 = 0
num2 = 1
inp = int(input("Enter how many digits of the Fibonacci Sequence you want: "))
for i in range(inp):
    print(num1, end=" ")
    num3 = num1 + num2
    num1 = num2
    num2 = num3