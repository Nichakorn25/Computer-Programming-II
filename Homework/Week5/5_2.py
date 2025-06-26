# 2.จงเขียนโปรแกรมเพื่อรับอีเมล 1 อีเมล แล้วส่งอีเมลนั้นไปที่ฟังก์ชัน check() ซึ่งจะทำการหาจำนวน 
# ตัวอักษรที่ไม่ใช่ตัวอักษร a-z หรือ A-Z ใส่ไว้ในลิสต์แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Enter an email: kacha@sut.ac.th
# Total non-character a-z or A-Z = 3
# They are ['@', '.', '.']


# Enter an email: K.chan-1999@gmail.com
# Total non-character a-z or A-Z = 8
# They are ['.', '-', '1', '9', '9', '9', '@', '.']


def check(email):
    non_char_list = []
    for ch in email:
        if not ch.isalpha():  
            non_char_list.append(ch)
            
    print("Total non-character a-z or A-Z =", len(non_char_list))
    print("They are", non_char_list)

email = input("Enter an email: ")
check(email)
