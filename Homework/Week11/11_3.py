# 3.จงเขียนโปรแกรมถามผู้ใช้ว่าต้องการป้อนเลขจำนวนเต็มกี่จำนวน ซึ่งจะต้องอยู่ในช่วง 5–20 เท่านั้น
# ถ้าไม่อยู่ในพิสัยให้แสดงข้อความว่า Invalid Number!!! แล้ววนรับข้อมูลใหม่จนกว่าจะได้ข้อมูลที่ต้องการ
# จากนั้นให้วนลูปรับข้อมูลเหล่านั้นเก็บไว้แบบลิสต์ในตัวแปร lst โดยข้อมูลที่จะรับเข้ามาเก็บไว้ในลิสต์นั้นจะต้องไม่ซ้ำกัน 
# ถ้าซ้ำจะต้องวนลูปรับข้อมุลใหม่และรับข้อมูลเลขจำนวนเต็มจากผู้ใช้ 1 ตัวเพื่อใช้เป็น key ในการค้นหาแบบแบ่งครึ่ง (Binary search)
# แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# ครั้งที่ 1
# How many number (5–20): 1  
# Invalid Number!!!  
# How many number (5–20): 25  
# Invalid Number!!!  
# How many number (5–20): 7  
# Number 1: 9  
# Number 2: 4  
# Number 3: 20  
# Number 4: 2  
# Number 5: 4  
# Invalid!!! 4 is already in the list  
# Number 5: 9  
# Invalid!!! 9 is already in the list  
# Number 5: 1  
# Number 6: 32  
# Number 7: 15  
# Original data: [9, 4, 20, 2, 1, 32, 15]  
# Sorted data: [1, 2, 4, 9, 15, 20, 32]  
# Enter a number to be searched: 4  
# Found '4' at index 2



while True:
    count = int(input("How many number (5–20): "))
    if 5 <= count <= 20:
        break
    print("Invalid Number!!!")

# รับข้อมูลตัวเลขไม่ซ้ำกัน
lst = []
while len(lst) < count:
    num = int(input(f"Number {len(lst)+1}: "))
    if num in lst:
        print(f"Invalid!!! {num} is already in the list")
    else:
        lst.append(num)

print("Original data:", lst)

# เรียงข้อมูลก่อนทำ binary search
lst.sort()
print("Sorted data:", lst)

# รับค่าที่ต้องการค้นหา
key = int(input("Enter a number to be searched: "))

# Binary Search
left = 0
right = len(lst) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if lst[mid] == key:
        print(f"Found '{key}' at index {mid}")
        found = True
        break
    elif key < lst[mid]:
        right = mid - 1
    else:
        left = mid + 1

if not found:
    print(f"Cannot find number {key}")
