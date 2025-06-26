# 3.จงเขียนโปรแกรมในการเรียกใช้ฟังก์ชัน get_input() ซึ่งจะรับชุดข้อมูลที่เป็นเลขจำนวนเต็มโดยข้อมูลแต่ละตัวจะถูกคั่นด้วยเครื่องหมายจุลภาค (,)
# และเก็บข้อมูลลงในลิสต์ตัวแปร lst แล้วเรียกใช้ฟังก์ชัน bubble_sort() ซึ่งจะทำการเรียงลำดับข้อมูลที่ฟังก์ชัน get_input() ได้รับเข้ามา
# แล้วแสดงผลออกที่จอภาพ ดังตัวอย่างการรันโปรแกรม
# *** แนะนำ ตัวแปร lst ถูกกำหนดเป็นแบบ global ในฟังก์ชัน get_input() และ bubble_sort()

# Function: get_input()  
# Enter 7 numbers separated by comma: 9,5,8,1,4,3,2  
# Data in list: ['9', '5', '8', '1', '4', '3', '2']

# Function: bubble_sort()  
# After Round 1: ['5', '8', '1', '4', '3', '2', '9']  
# After Round 2: ['5', '1', '4', '3', '2', '8', '9']  
# After Round 3: ['1', '4', '3', '2', '5', '8', '9']  
# After Round 4: ['1', '3', '2', '4', '5', '8', '9']  
# After Round 5: ['1', '2', '3', '4', '5', '8', '9']  
# After Round 6: ['1', '2', '3', '4', '5', '8', '9']  
# Sorted List: ['1', '2', '3', '4', '5', '8', '9']

def get_input():
    global lst
    lst = input("Enter 7 numbers separated by comma: ").split(",")
    print("Data in list:", lst)

def bubble_sort():
    global lst
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(f"After Round {i+1}:", lst)
    print("Sorted List:", lst)

# เรียกใช้งาน
print("Function: get_input()")
get_input()
print("\nFunction: bubble_sort()")
bubble_sort()
