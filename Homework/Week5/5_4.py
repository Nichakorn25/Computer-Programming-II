# 4. จงเขียนโปรแกรมเพื่อเรียกใช้ฟังก์ชัน get_input() ซึ่งทำหน้าที่รับข้อมูลเลขจำนวนเต็ม 1, 2 หรือ 0 เท่านั้น
# ถ้าไม่อยู่ในพิสัยให้แสดงข้อความว่า "Invalid Choice" แล้ววนลูปรับเลขจำนวนเต็มใหม่ เมื่อได้ข้อมูลที่ต้องการแล้ว
# โปรแกรมจะตรวจสอบว่า
#     - ถ้าผู้ใช้ป้อน 1 เข้ามาเลือก โปรแกรมจะเรียกใช้ฟังก์ชัน draw_triangle() เพื่อวาดรูปสามเหลี่ยมกลวง ดังตัวอย่างการรันโปรแกรม
#     - ถ้าผู้ใช้ป้อน 2 เข้ามาเลือก โปรแกรมจะเรียกใช้ฟังก์ชัน draw_square() เพื่อวาดรูปสี่เหลี่ยมกลวง ดังตัวอย่างการรันโปรแกรม
#     - ถ้าผู้ใช้ป้อน 0 เข้ามาเลือก โปรแกรมจะแสดงข้อความ "Bye Bye" แล้วจบโปรแกรม ดังตัวอย่างการรันโปรแกรม

# ครั้งที่ 1
# 1: Draw a triangle  
# 2: Draw a square  
# 0: Exit Program  
# Enter a choice of 1, 2 or 0: 7  
# Your choice is 7.  
# Invalid Choice  

# ครั้งที่ 2
# 1: Draw a triangle  
# 2: Draw a square  
# 0: Exit Program  
# Enter a choice of 1, 2 or 0: 1  
# Your choice is 1.  
# Draw a triangle  
# 1  
# 22  
# 3 3  
# 4   4  
# 55555  

# ครั้งที่ 3
# 1: Draw a triangle  
# 2: Draw a square  
# 0: Exit Program  
# Enter a choice of 1, 2 or 0: 2  
# Your choice is 2.  
# Draw a square  
# *****
# *   *
# *   *
# *   *
# *****

def get_input():
    print("1: Draw a triangle")
    print("2: Draw a square")
    print("0: Exit Program")
    choice = int(input("Enter a choice of 1, 2 or 0: "))
    return choice

def draw_triangle():
    print("Draw a triangle")
    for i in range(1, 6):
        if i == 1 or i == 2 or i == 3:
            print(str(i) * i)
        elif i == 4:
            print(str(i) + ' ' * (i - 2) + str(i))
        elif i == 5:
            print(str(i) * i)

def draw_square():
    print("Draw a square")
    for i in range(5):
        if i == 0 or i == 4:
            print("*" * 5)
        else:
            print("*" + " " * 3 + "*")

# ทำตรงนี้ก่อน
choice = get_input()
print("Your choice is", choice)

if choice == 1:
    draw_triangle()
elif choice == 2:
    draw_square()
elif choice == 0:
    print("Bye Bye")
else:
    print("Invalid Choice")
