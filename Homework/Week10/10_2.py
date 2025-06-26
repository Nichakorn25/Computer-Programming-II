# 2.จงเขียนโปรแกรมถามผู้ใช้ว่าต้องการป้อนข้อมูลเลขจำนวนเต็มกี่จำนวน ซึ่งจะต้องอยู่ในช่วง 5 ถึง 10 ตัวเท่านั้น
# ถ้าไม่อยู่ในพพิสัยให้แสดงข้อความว่า Invalid Number!!!
# แล้ววนรับข้อมูลใหม่จนกว่าจะได้ข้อมูลที่ต้องการ
# แล้วจบการวนลูปรับข้อมูลเหล่านั้นเก็บไว้ในแบบลิสต์ตัวแปร lst
# หลังจากนั้นให้ทำการเรียงลำดับข้อมูลในลิสต์ lst แบบเลือก (Selection Sort) แล้วแสดงออกที่จอภาพ
# ดังตัวอย่างการรันโปรแกรม

# How many number (5–10): 1  
# Invalid Number!!!  
# How many number (5–10): 20  
# Invalid Number!!!  
# How many number (5–10): 7  
# Number 1: 5  
# Number 2: 8  
# Number 3: 1  
# Number 4: 7  
# Number 5: 3  
# Number 6: 6  
# Number 7: 2  
# Original List: [5, 8, 1, 7, 3, 6, 2]  
# After Round 1: [1, 8, 5, 7, 3, 6, 2]  
# After Round 2: [1, 2, 5, 7, 3, 6, 8]  
# After Round 3: [1, 2, 3, 7, 5, 6, 8]  
# After Round 4: [1, 2, 3, 5, 7, 6, 8]  
# After Round 5: [1, 2, 3, 5, 6, 7, 8]  
# After Round 6: [1, 2, 3, 5, 6, 7, 8]  
# Sorted List: [1, 2, 3, 5, 6, 7, 8]

while True:
    count = int(input("How many number (5–10): "))
    if 5 <= count <= 10:
        break
    print("Invalid Number!!!")

lst = []
for i in range(count):
    num = int(input(f"Number {i+1}: "))
    lst.append(num)

print("Original List:", lst)

for i in range(len(lst) - 1):
    min_idx = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_idx]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(f"After Round {i+1}:", lst)

print("Sorted List:", lst)
