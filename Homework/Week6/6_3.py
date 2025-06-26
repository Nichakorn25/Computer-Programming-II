# 3.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 1 จำนวน แล้วส่งเลขจำนวนนั้นไปที่ฟังก์ชัน dec_2_hex() 
# ซึ่งจะทำการแปลงเลขฐานสิบ (Decimal Number) 
# ที่รับเข้ามาเป็นเลขฐานสิบหก (Hexadecimal Number) แบบวนซ้ำ (Recursive) แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Enter an integer: 3749  
# Decimal 3749 = EA5 Hexadecimal


def dec_2_hex(n):
    hex_chars = '0123456789ABCDEF'
    if n == 0:
        return ''
    else:
        return dec_2_hex(n // 16) + hex_chars[n % 16]

num = int(input("Enter an integer: "))
hex_str = dec_2_hex(num)
print(f"Decimal {num} = {hex_str if hex_str else '0'} Hexadecimal")
