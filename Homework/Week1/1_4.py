# 4.จงเขียนโปรแกรมการสร้างรูปสี่เหลี่ยมกลวงที่ระบุความกว้าง 7 ถึง 10 เท่านั้น
# ถ้าไม่อยู่ในพิสัยให้แสดงข้อความว่า Invalid Number! แล้ววนลูปรับใหม่จนกว่าจะได้ข้อมูลที่ต้องการ
# และความหนา(ขอบ) 1 ถึง 3 เท่านั้น ถ้าไม่อยู่ในพิสัยให้แสดงข้อความว่า Invalid Number!!! แล้ววนลูปรับใหม่จนกว่าจะได้ข้อมูลที่ต้องการ
# ดังตัวอย่างการรันโปรแกรม

# Width (7-10): 5
# Invalid Number!!!
# Width (7-10): 12
# Invalid Number!!!
# Width (7-10): 10
# Border (1-3): 0
# Invalid Number!!!
# Border (1-3): 2

# **********
# **********
# **      **
# **      **
# **      **
# **      **
# **      **
# **      **
# **********
# **********


while True:
    width = int(input("Width (7-10): "))
    if 7 <= width <= 10:
        break
    print("Invalid Number!!!")

while True:
    border = int(input("Border (1-3): "))
    if 1 <= border <= 3:
        break
    print("Invalid Number!!!")

height = width

for row in range(height):
    if row < border or row >= height - border:
        print("*" * width)
    else:
        print("*" * border + " " * (width - 2 * border) + "*" * border)