# 2.จงเขียนโปรแกรมการรับข้อมูลเบอร์โทรศัพท์มือถือ แปลงข้อมูลนั้นให้เป็นเซ็ต แล้วตรวจสอบว่ามีเลขใดที่ไม่ปรากฎอยู่ในเบอร์มือถือนั้น
# แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# Mobile number: 0894257777
# Your mobile is 0894257777.
# {'0','8','4','7','2','5','9'}
# Missing digit: {'6','1','3'}
# Total missing number = 3

# Mobile number: 0894251763
# Your mobile is 0894251763.
# {'0','8','9','4','2','5','1','7','6','3'}
# There is no missing any digit.


mobile = input("Mobile number: ")
print(f"Your mobile is {mobile}.")
mobile_set = set(mobile)
print(mobile_set)

all_digits = set('0123456789')

missing_digits = all_digits - mobile_set

if missing_digits:
    print(f"Missing digit: {missing_digits}")
    print(f"Total missing number = {len(missing_digits)}")
else:
    print("There is no missing any digit.")
