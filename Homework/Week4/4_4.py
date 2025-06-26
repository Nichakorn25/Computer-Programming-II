# 4.จงเขียนโปรแกรมโดยใช้ฟังก์ชัน range() ช่วยในการกำหนดให้ตัวแปร even เก็บเลขจำนวนเต็มที่เป็นเลขคู่
# ตั้งแต่ 20 ถึง 44 และตัวแปร odd เก็บเลขจำนวนเต็มที่เป็นเลขคี่ตั้งแต่ -5 ถึง -29 แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ***แนะนำ ฟังก์ชัน range(),len() และ sum()

# Even number from 20 to 44: 20 22 24 26 28 30 32 34 36 38 40 42 44
# There are 13 even numbers.
# Sum of all even numbers are 416.
# Odd numbers from -5 to -29: -5 -7 -9 -11 -13 -15 -17 -19 -21
# -23 -25 -27 -29
# There are 13 odd numbers.
# Sum of all odd numbers are -221.



even = list(range(20, 45, 2))
odd = list(range(-5, -30, -2))

print("Even number from 20 to 44:", *even)
print("There are", len(even), "even numbers.")
print("Sum of all even numbers are", sum(even) , ".")


print("Odd numbers from -5 to -29:", *odd)
print("There are", len(odd), "odd numbers.")
print("Sum of all odd numbers are", sum(odd) , ".")
