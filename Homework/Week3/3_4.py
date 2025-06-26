# 4.จงเขียนโปรแกรมในการรับชุดข้อมูลที่เป็นเลขจำนวนเต็ม 5 ตัว คือ 3 9 5 1 7 แต่ละตัวคั่นด้วยช่องว่าง 1 ช่อง
# นำข้อมูลนั้นเก็บเป็นลิสต์ไว้ที่ตัวแปร s หลังจากนั้น
#     ขั้นตอนที่ 1:เพิ่มเลขจำนวนเต็ม 8 และ 4 ต่อท้ายข้อมูลเดิม ข้อมูลจะเปลียนเป็น 3 9 5 1 7 8 4
#     ขั้นตอนที่ 2:แทรกเลขจำนวนเต็ม 2 ไปอยู่หลังเลข 3 และ 6 ไปอยู่หลังเลข 5
#               ข้อมูลจะเปลี่ยนเป็น 3 2 9 5 6 1 7 8 4
#     ขั้นตอนที่ 3:ลบเลขจำนวนเต็ม 1 และ 8 ทิ้ง ข้อมูลจะเปลี่ยนไปเป้ฯ 3 2 9 5 6 7 4

# Enter 5 numbers seperated by space: 3 9 5 1 7
# Original: [3,9,5,1,7]
# Step 1:Add 8 and 4 to the end of the list
#        [3,9,5,1,7,8,4]
# Step 2:Insert 2 after 3 and 6 after 5
#        [3,2,9,5,6,1,7,8,4]
# Step 3: Remove 1 and 8
#        [3,2,9,5,6,7,4]


input_str = input("Enter 5 numbers seperated by space: ")
s = list(map(int, input_str.split()))
print("Original:", s)

# ---------- Step 1 ----------
print("Step 1: Add 8 and 4 to the end of the list")
s.append(8)
s.append(4)
print("       ", s)

# ---------- Step 2 ----------
print("Step 2: Insert 2 after 3 and 6 after 5")

index_3 = s.index(3)
s.insert(index_3 + 1, 2)

index_5 = s.index(5)
s.insert(index_5 + 1, 6)

print("       ", s)

# ---------- Step 3 ----------
print("Step 3: Remove 1 and 8")
s.remove(1)
s.remove(8)
print("       ", s)
