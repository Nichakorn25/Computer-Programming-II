# 1.จงเขียนโปรแกรมการกำหนดตัวแปร t1 เก็บข้อมูลแบบทูเพิลประกอบด้วย 1,3,5,7 และ 9 
# และตัวแปร t2 เก็บข้อมูล 0,2,4,6  และ 8 แล้วหาผลบวกของข้อมูลทั้ง 2 ทูเพิลที่มีอินเด็กซ์เดียวกันไปเก็บไว้ที่ตัวแปร sum 
# แล้วแสดงข้อมูลทั้ง 3 ทูเพิล ออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม

# t1 = (1,3,5,7,9)
# t2 = (0,2,4,6,8)
# sum = (1,5,9,13,17)


t1 = (1, 3, 5, 7, 9)
t2 = (0, 2, 4, 6, 8)

sum_list = []

for i in range(len(t1)):
    s = t1[i] + t2[i]
    sum_list.append(s)

sum = tuple(sum_list)

print("t1 =", t1)
print("t2 =", t2)
print("sum =", sum)
