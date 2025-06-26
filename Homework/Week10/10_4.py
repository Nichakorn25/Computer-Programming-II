# 4.จงเขียนโปรแกรมในการเรียกใช้ฟังก์ชัน get_input() ซึ่งจะรับข้อมูลที่เป็นสตริงเข้ามา แล้วเก็บไว้ที่ตัวแปร s
# แล้วเรียกใช้ฟังก์ชัน selection_sort() ซึ่งจะทำการเรียงลำดับข้อมูลที่ฟังก์ชัน get_input() ได้รับเข้ามา แล้วแสดงผลออกที่จอภาพ
# ดังตัวอย่างการรันโปรแกรม
# *** แนะนำ ตัวแปร s ถูกกำหนดเป็นแบบ global ในฟังก์ชัน get_input() และ selection_sort()

# Function: get_input()  
# Enter a string: thailand  
# Original string: thailand

# Function: selection_sort()  
# After Round 1: ['a', 'h', 't', 'i', 'l', 'a', 'n', 'd']  
# After Round 2: ['a', 'a', 't', 'i', 'l', 'h', 'n', 'd']  
# After Round 3: ['a', 'a', 'd', 'i', 'l', 'h', 'n', 't']  
# After Round 4: ['a', 'a', 'd', 'h', 'l', 'i', 'n', 't']  
# After Round 5: ['a', 'a', 'd', 'h', 'i', 'l', 'n', 't']  
# After Round 6: ['a', 'a', 'd', 'h', 'i', 'l', 'n', 't']  
# After Round 7: ['a', 'a', 'd', 'h', 'i', 'l', 'n', 't']  
# Sorted List: ['a', 'a', 'd', 'h', 'i', 'l', 'n', 't']

def get_input():
    global s
    s = input("Enter a string: ")
    print("Original string:", s)

def selection_sort():
    global s
    lst = list(s)
    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        print(f"After Round {i+1}:", lst)
    print("Sorted List:", lst)

# เรียกใช้งาน
print("Function: get_input()")
get_input()
print("\nFunction: selection_sort()")
selection_sort()
