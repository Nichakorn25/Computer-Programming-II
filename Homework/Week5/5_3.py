# 3.จงเขียนโปรแกรมเพื่อเรียกใช้ฟังก์ชัน get_input() ซึ่งทำหน้าที่รับข้อมูลเข้ามา 1 สตริง เก็บไว้ที่ตัวแปร s แล้วแสดงข้อความที่ออกมา
# หลังจากนั้นในโปรแกรมจะเรียกใช้งานฟังก์ชัน change_case() โดยส่งข้อมูลของตัวแปร s ไป ซึ่งทำหน้าที่ตรวจสอบข้อมูลในตัวแปร s
# ถ้าพบว่าเป็นตัวอักษรเล็ก (a-z) ให้เปลี่ยนเป็นตัวอักษรใหญ่ (A-Z)
# ถ้าเป็นตัวอักษรใหญ่ให้เปลี่ยนเป็นตัวอักษรเล็ก
# ถ้าเป็นตัวอักษรอื่นใดให้คงเดิมไว้
# แล้วแสดงข้อมูลสตริงที่เกิดขึ้น พร้อมกับบอกจำนวนของการเปลี่ยนแปลงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Enter a string: SUT–Thai 2024
# You entered "SUT–Thai 2024".
# New string is "sut–tHAI 2024".
# Total change = 7

# Enter a string: TH: Thailand
# You entered "TH: Thailand".
# New string is "th: tHAILAND".
# Total change = 10

def get_input():
    return input("Enter a string: ")

def change_case(s):
    new_str = ''
    change_count = 0

    for ch in s:
        if ch.islower():         
            new_str += ch.upper()
            change_count += 1
        elif ch.isupper():    
            new_str += ch.lower()
            change_count += 1
        else:                   
            new_str += ch

    print(f'You entered "{s}".')
    print(f'New string is "{new_str}".')
    print(f'Total change = {change_count}')

# เรียกใช้งาน
s = get_input()
change_case(s)
