# 4.จงเขียนโปรแกรมรับคำศัพท์(Word) ตั้งแต่ 3 ถึง 5 คำเท่านั้น ถ้าไม่อยู่ในพิสัยให้วนลูปรับจำนวนคำสัพท์ใหม่จนกว่าจะได้ข้อมูลที่ต้องการ
# หลังจากนั้นให้วนลูปรับคำศัพท์เหล่านั้นโดยจัดเก็บไว้ในลิสต์ แสดงข้อมูลทั้งหมดในลิสต์และแสดงคำศัพท์ที่มีความยาวที่สุดออกที่จอภาพ
# ดังตัวอย่างการรันโปรแกรม

# How many word? (3-5): 1
# Invalid number!!!
# How many word? (3-5): 10
# Invalid number!!!
# How many word? (3-5): 3
# Word 1: Suranaree
# Word 2: Environment
# Word 3: Computer
# Data in the list: ['Suranaree','Environment','Computer']
# Longest word is "Environment".


while True:
    num_words = int(input("How many word? (3-5): "))
    if 3 <= num_words <= 5:
        break
    else:
        print("Invalid number!!!")

word_list = []

for i in range(1, num_words + 1):
    word = input(f"Word {i}: ")
    word_list.append(word)

print("Data in the list:", word_list)

longest_word = max(word_list, key=len)

print(f'Longest word is "{longest_word}".')
