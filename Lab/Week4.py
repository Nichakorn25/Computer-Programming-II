# 1.❑ ฟังก์ชันสําเร็จรูป (Built-in Functions)
# 1. จงแสดงผลลัพธ์ของโปรแกรมต่อไปนี้ แล้วเขียนโปรแกรมเพื่อตรวจสอบความถูกต้อง
# 1. x = list(range(4))
# 2. y = list(range(1,7,1))
# 3. z = list(range(-2,-10,-2))
# 4. print(x)
# 5. print(y)
# 6. print(z)

# 4: [0, 1, 2, 3]
# 5: [1, 2, 3, 4, 5, 6]
# 6: [-2, -4, -6, -8]

#==================================================================

# 2. จงแสดงผลลัพธ์ของโปรแกรมต่อไปนี้ แล้วเขียนโปรแกรมเพื่อตรวจสอบความถูกต้อง
# 1. num = [3,5,2,4,1]
# 2. s = 'COMPRO'
# 3. fruit = {'Apple':300, 'durian':100, 'Coconat':400, 'Banana':200,}
# 4. print(min(num))
# 5. print(max(num))
# 6. print(sum(num))
# 7. print(pow(num[2],4))
# 8. print(sorted(num))
# 9. print(sorted(num, reverse=True))
# 10. print(len(s))
# 11. print(sorted(s))
# 12. print(sorted(s, reverse=True))
# 13. print(max(fruit))
# 14. print(max(fruit.values()))
# 15. print(list(fruit))


# 4: 1
# 5: 5
# 6: 15
# 7: 16
# 8: [1, 2, 3, 4, 5]
# 9: [5, 4, 3, 2, 1]
# 10: 6
# 11: ['C', 'M', 'O', 'O', 'P', 'R']
# 12: ['R', 'P', 'O', 'O', 'M', 'C']
# 13: durian
# 14: 400
# 15: ['Apple', 'durian', 'Coconat', 'Banana']

#==================================================================

# 3. จงเขียนโปรแกรมในการกำหนดตัวแปร s = ‘I love SUT.’ แล้วแสดงข้อมูลโดยใช้ฟังก์ชัน
# slice() แยกแต่ละคำออกมา แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# 01234567890123456
# I love SURANAREE.
# #Used slice() funtions
# I
# love
# SURANAREE.


# print('01234567890123456')
# s = 'I love SURANAREE.'
# print(s)
# print('\n#Used slice() funtions')
# print(s[slice(1)])
# print(s[slice(2,6)])
# print(s[slice(7,17)])
