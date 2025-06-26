# 4.จงเขียนโปรแกรมในการกำหนดตัวแปร s = 'BANGPRETOY' แล้วรับข้อมูลตัวอักษรจากผู้ใช้ 1 ตัว เพื่อใช้เป็น key 
# ในการค้นหาแบบแบ่งครึ่ง (Binary Search) แล้วแสดงผลออกที่จอภาพ

# Original data: BANGPRETOY  
# Sorted data: ['A', 'B', 'E', 'G', 'N', 'O', 'P', 'R', 'T', 'Y']  
# Enter a character to be searched: K  
# Cannot find 'K'

# Original data: BANGPRETOY  
# Sorted data: ['A', 'B', 'E', 'G', 'N', 'O', 'P', 'R', 'T', 'Y']  
# Enter a character to be searched: P  
# Found 'P' at index 6


s = "BANGPRETOY"
lst = sorted(list(s))

print("Original data:", s)
print("Sorted data:", lst)

key = input("Enter a character to be searched: ")

left, right = 0, len(lst) - 1
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
    print(f"Cannot find '{key}'")
