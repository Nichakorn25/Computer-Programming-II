# 1.จงเขียนโปรแกรมการรับข้อมูล 25,13,65,70,58,4,10 เข้ามาเก็บไว้ที่ตัวแปร s ทำการแปลงข้อมูลในตัวแปร s
# ให้เป็นลิสต์ที่เ็บเลขจำนวนเต็ม ทำการหาผลรวมของเลขเหล่านั้นโดยใช้ลูป for แล้วแสดงออกที่จอภาพ  ดังตัวอย่างการรันโปรแกรม

# Enter numbers seperated by comma: 25,13,65,70,58,4,10
# s : [25,13,65,70,58,4,10]
# Sum of all numbers in s = 245


input_str = input("Enter numbers seperated by comma: ")
s = input_str.split(",")        
s = [int(num) for num in s]   

print("s :", s)

total = 0
for num in s:
    total += num

print("Sum of all numbers in s =", total)
