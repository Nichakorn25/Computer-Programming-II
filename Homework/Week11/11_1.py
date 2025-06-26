# 1.จงเขียนโปรแกรมในการกำหนดตัวแปร s = 'ANIMALS' แล้วรับข้อมูลตัวอักษรจากผู้ใช้ 1 ตัว เพื่อใช้เป็น key 
# ในการค้นหาแบบเส้นตรง (Linear Search) แล้วแสดงผลออกที่จอภาพ

# Enter a character to be searched: K  
# Cannot find 'K'

# Enter a character to be searched: A  
# Found 'A' at index 0

s = 'ANIMALS'
key = input("Enter a character to be searched: ")

found = False
for i in range(len(s)):
    if s[i] == key:
        print(f"Found '{key}' at index {i}")
        found = True
        break

if not found:
    print(f"Cannot find '{key}'")
