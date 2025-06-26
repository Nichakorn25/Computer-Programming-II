# 3.จงเขียนโปรแกรมในการรับกลุ่มข้อมูลเลขจำนวนเต็ม แต่ละตัวจะคั่นด้วยช่องว่าง 1 ช่อง
# หลังจากนั้นให้แสดงข้อมูลเหล่านั้นออกทางจอภาพ ทำการเรียงข้อมูลแบบย้อนกลับ (reverse order)
# ทำการเรียงลำดับข้อมูลจากน้อยไปมาก แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ***แนะนำ นำข้อมูลไปเก็บไว้ในลิสต์ ใช้เมธอด .reverse() และ .sort()

# Enter in number seperated by a space: 3 1 5 9 4 8
# Data in original order: ['3','1','5','9','4','8']
# Data in reverse order: ['8','4','9','5','1','3']
# Data in descending order: ['1','3','4','5','8','9']


input_str = input("Enter in number seperated by a space: ")
data = input_str.split()

print("Data in original order:", data)

reversed_data = data.copy()
reversed_data.reverse()
print("Data in reverse order:", reversed_data)

sorted_data = data.copy()
sorted_data.sort(key=int)  # เรียงลำดับแบบตัวเลข
print("Data in descending order:", sorted_data)
