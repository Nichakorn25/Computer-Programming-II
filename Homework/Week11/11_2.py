# 2.จงเขียนโปรแกรมถามผู้ใช้ว่าต้องการป้อนเลขจำนวนเต็มกี่จำนวน ซึ่งจะต้องอยู่ในช่วง 5–20 จำนวนเท่านั้น
# ถ้าไม่อยู่ในช่วงให้แสดงข้อความว่า Invalid Number!!!
# แล้ววนรับข้อมูลใหม่จนกว่าจะได้ข้อมูลที่ต้องการ
# หลังจากนั้นให้วนลูปรับข้อมูลเก็บไว้ในลิสต์ตัวแปร lst
# และรับข้อมูลเลขจำนวนเต็มจากผู้ใช้ 1 ตัว เพื่อใช้เป็น key ในการค้นหาแบบเส้นตรง (Linear Search)
# แล้วแสดงผลออกที่จอภาพ

# ครั้งที่ 1
# How many number (5–20): 1  
# Invalid Number!!!  
# How many number (5–20): 30  
# Invalid Number!!!  
# How many number (5–20): 6  
# Number 1: 1  
# Number 2: 2  
# Number 3: 3  
# Number 4: 7  
# Number 5: 3  
# Number 6: 2  
# Enter a number to be searched: 2  
# Found number 2 at index 1  
# Found number 2 at index 4  
# Total found = 2

# ครั้งที่ 2
# How many number (5–20): 5  
# Number 1: 1  
# Number 2: 2  
# Number 3: 3  
# Number 4: 4  
# Number 5: 5  
# Enter a number to be searched: 9  
# Cannot find number 9

while True:
    count = int(input("How many number (5–20): "))
    if 5 <= count <= 20:
        break
    print("Invalid Number!!!")

lst = []
for i in range(count):
    num = int(input(f"Number {i+1}: "))
    lst.append(num)

key = int(input("Enter a number to be searched: "))
found = False
found_count = 0

for i in range(len(lst)):
    if lst[i] == key:
        print(f"Found number {key} at index {i}")
        found = True
        found_count += 1

if found:
    print(f"Total found = {found_count}")
else:
    print(f"Cannot find number {key}")
