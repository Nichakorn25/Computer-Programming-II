# 2. จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 1 จำนวน แล้วส่งเลขจำนวนนั้นไปที่ฟังก์ชัน dec_2_oct() 
# ซึ่งจะทำการแปลงเลขฐานสิบ (Decimal Number) ที่รับเข้ามาเป็นเลขฐานแปด (Octal Number) 
# แบบวนซ้ำ (Recursive) แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Enter an integer: 1463  
# Decimal 1463 = 2667 Octal


def dec_2_oct(n):
    if n == 0:
        return ''
    else:
        return dec_2_oct(n // 8) + str(n % 8)

num = int(input("Enter an integer: "))
octal = dec_2_oct(num)
print(f"Decimal {num} = {octal if octal else 0} Octal")
