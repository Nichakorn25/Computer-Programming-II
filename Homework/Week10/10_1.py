# 1.จงเขียนโปรแกรมในการรับข้อมูลสตริง 1 สตริง ทำการเรียงลำดับแบบฟองสบู่ (Bubble sort) 
# แล้วแสดงออกที่จอภาพดังตัวอย่างการรันโปรแกรม

# Enter a string: avocado  
# Original String = avocado  
# Using function sorted(): ['a', 'a', 'c', 'd', 'o', 'o', 'v']  
# Convert string to list: ['a', 'v', 'o', 'c', 'a', 'd', 'o']  
  
# Using Bubble Sort  
# After Round 1: ['a', 'o', 'c', 'a', 'd', 'o', 'v']  
# After Round 2: ['a', 'c', 'a', 'd', 'o', 'o', 'v']  
# After Round 3: ['a', 'a', 'c', 'd', 'o', 'o', 'v']  
# After Round 4: ['a', 'a', 'c', 'd', 'o', 'o', 'v']  
# After Round 5: ['a', 'a', 'c', 'd', 'o', 'o', 'v']  
# After Round 6: ['a', 'a', 'c', 'd', 'o', 'o', 'v']  
# Sorted List: ['a', 'a', 'c', 'd', 'o', 'o', 'v']

s = input("Enter a string: ")
print("Original String =", s)

sorted_str = sorted(s)
print("Using function sorted():", sorted_str)

lst = list(s)
print("Convert string to list:", lst)

print("\nUsing Bubble Sort")
n = len(lst)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(f"After Round {i+1}:", lst)

print("Sorted List:", lst)
