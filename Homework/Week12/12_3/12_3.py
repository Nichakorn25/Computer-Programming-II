# 3.จงเขียนโปรแกรมเพื่อเขียนข้อมูลลงแฟ้มข้อมูลแบบซีเอสวี ลงในไฟล์ worker.csv 
# ซึ่งแต่ละเรคอร์ดจะประกอบไปด้วย ชื่อ อายุ อีเมล เบอร์โทรศัพท์ และเพศ ดังแสดงในรูปที่ 10.2 และ 10.3

# ตัวอย่างในไฟล์ worker.csv:
# Preecha,32,preecha@gmail.com,0894257777,Male
# Dara,28,dara_dara@gmail.com,0866442277,Female
# Busara,29,b_sara@yahoo.com,0991112229,Female
# Suradej,41,dej_2020@gmail.com,0959595111,Male

data = [
    ["Preecha", 32, "preecha@gmail.com", "0894257777", "Male"],
    ["Dara", 28, "dara_dara@gmail.com", "0866442277", "Female"],
    ["Busara", 29, "b_sara@yahoo.com", "0991112229", "Female"],
    ["Suradej", 41, "dej_2020@gmail.com", "0959595111", "Male"]
]

with open("worker.csv", "w") as f:
    for record in data:
        f.write(",".join(map(str, record)) + "\n")
