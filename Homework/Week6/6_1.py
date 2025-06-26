# 1.จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 1 จำนวนที่เป็นเลขคู่ (even number) เท่านั้น 
# ถ้าไม่อยู่ในเงื่อนไขให้แสดงข้อความว่า "Invalid Number" แล้ววนลูปรับข้อมูลใหม่ เมื่อต้องอยู่ที่ต้องการแล้ว
# ให้ส่งเลขจำนวนเต็มนั้นไปที่ฟังก์ชัน sum_of_even() ซึ่งจะทำการหาผลรวมของเลขจำนวนเต็มนั้นไปจนถึง 2 แบบวนซ้ำ (Recursive) 
# แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Enter an even number: 25  
# Invalid Number  
# Enter an even number: 8  
# 8+6+4+2 = 20

# Enter an even number: 14  
# 14+12+10+8+6+4+2 = 56


def sum_of_even(n):
    if n == 0:
        return 0
    print(n, end='')
    if n > 2:
        print("+", end='')
    return n + sum_of_even(n - 2)

while True:
    num = int(input("Enter an even number: "))
    if num % 2 != 0:
        print("Invalid Number")
    else:
        print()
        result = sum_of_even(num)
        print(" =", result)
        break
