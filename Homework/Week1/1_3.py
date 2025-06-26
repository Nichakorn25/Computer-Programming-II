# 3.จงเขียนโปรแกรมการคำนวณค่าจอดรถของห้างสรรพสินค้าแห่งหนึ่ง รับข้อมูลเวลารถเข้าและเลารถออก 
# โดยมีเงงื่อนไขในการคิดค่าจอดรถดังนี้
#  - จอดฟรี 30 นาทีแรก
#  - 2 ชั่วโมงแรก 40 บาท (เศษนาที ปัดเป็น 1 ชั่วโมง) ชั่วโมงถัดไป ชั่วโใงละ 100 บาท
#  - 6 ชั่วโมง คิด 500 บาท
#  - 6 ชั่วโมงขึ้นไปจะคิดเต็มวัน คือ 2000 บาท

# ตัวอย่างการรันโปรแกรม
# Time in: 13.10
# Time out: 13.20
# You parked in for 0 hour(s) and 10 minute(s).
# You will not be charged !!!.
# You will pay 0 baht.

# Time in: 17.05
# Time out: 19.00
# You parked in for 1 hour(s) and 55 minute(s).
# You will be charged for the first 2 hour(s).
# You will pay 40 baht.

# Time in: 10.10
# Time out: 16.10
# You parked in for 6 hour(s) and 0 minute(s).
# You will be charged for 6 hour(s).
# You will pay 500 baht.

# Time in: 12.15
# Time out: 21.00
# You parked in for 8 hour(s) and 45 minute(s).
# You will be charged for the maximum rate.
# You will pay 2000 baht.


import math

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split('.'))
    return hours * 60 + minutes

time_in = input("Time in: ")
time_out = input("Time out: ")

in_minutes = time_to_minutes(time_in)
out_minutes = time_to_minutes(time_out)

total_minutes = out_minutes - in_minutes
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"You parked in for {hours} hour(s) and {minutes} minute(s).")

if total_minutes <= 30:
    print("You will not be charged !!!.")
    print("You will pay 0 baht.")
elif total_minutes <= 120:
    print("You will be charged for the first 2 hour(s).")
    print("You will pay 40 baht.")
elif total_minutes < 360:
    total_hours = math.ceil(total_minutes / 60)
    extra_hours = total_hours - 2
    total_fee = 40 + (extra_hours * 100)
    print(f"You will be charged for {total_hours} hour(s).")
    print(f"You will pay {total_fee} baht.")
elif total_minutes == 360:
    print("You will be charged for 6 hour(s).")
    print("You will pay 500 baht.")
else:
    print("You will be charged for the maximum rate.")
    print("You will pay 2000 baht.")
