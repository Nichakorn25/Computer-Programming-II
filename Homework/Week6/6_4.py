# 4.จงเขียนโปรแกรมเพื่อกำหนดให้ตัวแปรแบบลิสต์ lst = [1,2,3,4,5,6,7,8,9] และตัวแปร s = 'Korat' 
# แล้วสร้างฟังก์ชันแลมบ์ดา ทำหน้าที่แสดงสตริงออก 2 ครั้งเก็บไว้ที่ตัวแปร output2time 
# และทำหน้าที่แสดงค่าเฉลี่ยของลิสต์ lst เก็บไว้ที่ตัวแปร avg แล้วแสดงข้อมูลเหล่านั้นออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# 5.0  
# KoratKorat


def output2time(text):
    print(text * 2)

def avg(lst):
    return sum(lst) / len(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 'Korat'

print(avg(lst))
output2time(s)
