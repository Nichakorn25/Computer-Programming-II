# 2.จงเขียนโปรแกรมรับคำศัพท์ 1 คำ ทำการคำนวณหาความถี่ของตัวอักษรในคำศัพท์นั้น เก็บข้อมูลทั้งตัวอักษร และความถี่ไว้ในดิกชันนารี
# แล้วแสดงข้อมูลนั้นออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ***แนะนำใช้เมธอด .keys()

# Please enter a string: banana
# Data in dictionary: {'b':1,'a':3,'n':2}


word = input("Please enter a string: ")
freq_dict = {}

for ch in word:
    if ch in freq_dict:
        freq_dict[ch] += 1
    else:
        freq_dict[ch] = 1

print("Data in dictionary:", freq_dict)
