# ❑ การสร้างฟังก์ชันขึ้นใช้งานเอง (User-defined Functions)
# 1. จงเขียนโปรแกรมโดยใช้ลูป for ในการเรียกฟังก์ชัน welcome() ซึ่งจะแสดงข้อความ “Welcome
# to SUT.” ออกที่จอภาพ จำนวน 5 ครั้ง ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Welcome to SUT.
# Welcome to SUT.
# Welcome to SUT.
# Welcome to SUT.
# Welcome to SUT.


# No argument, no return
def welcome():
    print('Welcome to SUT.')
for i in range(5):
    welcome()

#==================================================================

# 2. จงเขียนโปรแกรมโดยกำหนดให้เรียกฟังก์ชัน getSentence() รับข้อความ 1 ข้อความ แล้วส่ง
# ข้อความนั้นกลับเพื่อหาจำนวนช่องว่าง แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Enter a sentence: I love SUT.
# Count of spaces is 2.

# No argument but return
def getSentence():
    x = (input('Enter a sentence: '))
    return x
s = getSentence()
count = 0
for i in s:
    if i==' ':
        count += 1
print('Count of spaces is %d.' % (count))

#==================================================================

# 3. จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 1 จำนวน แล้วส่งเลขจำนวนเต็มนั้นไปที่ฟังก์ชัน
# displaySum() ซึ่งจะทำการหาผลรวมตั้งแต่ 1 ถึงเลขจำนวนนั้น แล้วแสดงออกที่จอภาพ ดัง
# ตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Enter a number: 25
# Sum of all numbers from 1 to 25 is 325.


# Argument without return
def displaySum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print('Sum of all numbers from 1 to %d is %d.' % (n, sum))

n = int(input('Enter a number: '))
displaySum(n)

#==================================================================

# 4. จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็ม 2 จำนวน แล้วส่งเลขจำนวนเต็มทั้ง 2 จำนวนนั้นไปที่
# ฟังก์ชัน getMultiply() ซึ่งจะทำการคำนวณหาผลคูณ แล้วส่งผลคูณนั้นกลับเพื่อแสดงออกที่
# จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Enter a number 1: 5
# Enter a number 2: 12
# Result 5*12 = 60


# Argument with return
def getMultiply(x, y) :
    z = x * y
    return z
n1 = int(input('Enter a number1: '))
n2 = int(input('Enter a number2: '))
result = getMultiply(n1, n2)
print('Result %d*%d = %d' % (n1, n2, result))

#==================================================================

# ❑ อาร์กิวเมนต์ค่าปริยาย (Default Argument)
# 5. จงเขียนโปรแกรมเพื่อกำหนดให้ ฟังก์ชัน showClassroom() มีอาร์กิวเมนต์ค่าปริยายเป็น
# “Computer Lab” จากนั้นรับสตริง 1 สตริง แล้วส่งสตริงนั้นไปที่ฟังก์ชัน showClassroom()
# และเรียกใช้ฟังก์ชัน showClassroom() อีกครั้งโดยไม่ส่งสตริงไป ซึ่งจะแสดงผลที่จอภาพ ดัง
# ตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรม
# Which classroom do you study: lab8
# --- Show Argument ---
# You study in "lab8".
# --- Show default Argument ---
# You study in "Computer Lab".


def showClassroom(str='Computer Lab'):
 print('You study in "%s".' % str)
lab = input('Which classroom do you study: ')
print('\n--- Show Argument ---')
showClassroom(lab)
print('\n--- Show default Argument ---')
showClassroom()

#==================================================================

# ❑ โจทย์พิเศษ
# 6. จงเขียนโปรแกรมเพื่อกำหนดให้ตัวแปรแบบดิกชันนารี host = {'Rio_de_Janeiro': 2016,
# Tokyo': 2020, 'Paris': 2024, 'Milan': 2028} และรับข้อมูลเป็นปี ค.ศ. แล้วตรวจสอบว่าปีนั้น
# มีการจัดโอลิมปิคหรือไม่ ถ้ามีการจัดโอลิมปิคในปีนั้นให้ส่ง host และปีที่รับมา ไปที่ฟังก์ชัน
# city_in_year() เพื่อแสดงเมืองที่ใช้จัดการแข่งขัน แต่ถ้าไม่มีการจัดโอลิมปิคในปีนั้น ให้แสดง
# ข้อความว่า “No Olympic.” แล้วแสดงออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# ตัวอย่างการรันโปรแกรมครั้งที่ 1
# Year Of Olympic: 2024
# Oylmpic 2024 in Beijing
# ตัวอย่างการรันโปรแกรมครั้งที่ 2
# Year Of Olympic: 2023
# No Olympic.

def city_in_year(h,y):
    city = list(h.keys())
    year = list(h.values())
    index = year.index(y)
    print('Oylmpic %d in %s' %(y,city[index]))

host = {'Tokyo':2020,'Beijing':2024,'Paris':2024 ,'Milan':2028}
year = int(input('Year Of Olympic : '))
year_list = list(host.values())
x = year_list.count(year)
if x > 0 :
    city_in_year(host,year)
else :
    print('No Olympic.')