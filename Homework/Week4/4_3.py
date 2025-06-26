# 3.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 1 จำนวนแล้วแปลงจำนวนเต็มนั้นให้เป็นเลขฐานสอง
# ฐานแปด และฐานสิบหก แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ***แนะนำ ฟังก์ชัน bin(),oct(),hex()

# Enter a number: 25
# Based 10 = 25
# Based 2 = 0b11001
# Based 8 = 0o31
# Based 16 = 0x19

number = int(input("Enter a number:"))
print("Based 10 = ",number)
print("Based 2 = ",(bin(number)))
print("Based 8 = ",(oct(number)))
print("Based 16 = ",(hex(number)))
