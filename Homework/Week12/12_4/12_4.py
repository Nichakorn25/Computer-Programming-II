# 4.จงเขียนโปรแกรมเพื่ออ่านข้อมูลในไฟล์ worker.csv แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม:
# Name     Age  E-mail                   Mobile       Sex
# Preecha  32   preecha@gmail.com       0894257777   Male
# Dara     28   dara_dara@gmail.com     0866442277   Female
# Busara   29   b_sara@yahoo.com        0991112229   Female
# Suradej  41   dej_2020@gmail.com      0959595111   Male

print(f"{'Name':<8} {'Age':<4} {'E-mail':<25} {'Mobile':<12} {'Sex'}")

with open("worker.csv", "r") as f:
    for line in f:
        name, age, email, mobile, sex = line.strip().split(",")
        print(f"{name:<8} {age:<4} {email:<25} {mobile:<12} {sex}")
