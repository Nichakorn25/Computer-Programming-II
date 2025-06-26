from my_factorial import Fac

fac = Fac()
while True:
    num = int(input("Enter a number (1–100): "))
    if 1 <= num <= 100:
        break
    print("Invalid Input!!!")

print("Calculate Factorial Using Loop")
fac.loop(num)

print("Calculate Factorial Using Recursion")
print(f"{num}! = {'*'.join(str(i) for i in range(num, 0, -1))}")
print(f"{num}! = {fac.recursive(num)}")
