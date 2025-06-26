# 1.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 1 จำนวน แล้วส่งไปที่ฟังก์ชัน power_of_two() 
# เพื่อสร้างข้อมูลแบบลิสต์ขึ้นมา 1 ตัว โดยเริ่มจาก 1 ถึงเลขจำนวนเต็มนั้น แล้วแสดงออกที่จอภาพ 
# หลังจากนั้นจงสร้างข้อมูลแบบลิสต์ขึ้นมาใหม่อีก 1 ตัว
# ประกอบไปด้วยข้อมูลที่เป็นเลขยกกำลังสองของข้อมูลลิสต์ตัวแรก และแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# n = 8
# Original list: [1, 2, 3, 4, 5, 6, 7, 8]
# New power-of-two list: [1, 4, 9, 16, 25, 36, 49, 64]


def power_of_two(n):
    original_list = list(range(1, n + 1))
    power_list = [x**2 for x in original_list]
    
    print("Original list:", original_list)
    print("New power-of-two list:", power_list)

n = int(input("Enter a number: "))
power_of_two(n)
