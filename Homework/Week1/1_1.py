# 1.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 3 จำนวน โดยแ่ตละจำนวนจะไม่ซ้ำกัน 
# ทำการหาเลขที่มีค่าอยู่ระหว่างกลางแล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรัยโปรแกรม

# Enter number 1: 7
# Enter number 2: 9
# Enter number 3: 1
# The middle number of 7, 9 and 1 is 7.

# Enter number 1: 3
# Enter number 2: 5
# Enter number 3: 7
# The middle number of 3, 5 and 7 is 5.

# Enter number 1: 15
# Enter number 2: 30
# Enter number 3: 26
# The middle number of 15, 30 and 26 is 26.


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

numbers = [num1, num2, num3]
numbers.sort()

middle = numbers[1]

print(f"The middle number of {num1}, {num2} and {num3} is {middle}.")
