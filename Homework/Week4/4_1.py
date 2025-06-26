# 1.จงเขียนโปรแกรมรับประโยค 1 ประโยค หาจำนวนตัวอักษรและตัวเลข แล้วแสดงออกที่จอภาพ 
# ดังตัวอย่างการรันโปรแกรม 
# ***แนะนำ เมธอด .isalpha() และ .isdigit()

# Enter a sentence: I am 21 years old.
# "I am 21 years old."
# contains 11 letter(s) and 2 digit(s)



sentence = input("Enter a sentence: ")

letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"\"{sentence}\"")
print(f"contains {letter_count} letter(s) and {digit_count} digit(s)")
