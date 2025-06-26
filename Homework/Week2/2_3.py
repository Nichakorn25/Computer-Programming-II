# 3.จงเขียนโปรแกรมการสร้างดิกชันนารี ซึ่งประกอบด้วยคีย์(key) จากเลขจำนวนเต็ม 1 ถึง N 
# แต่ละคีย์จะมีค่า(value)เป็นสตริงของเลขจำนวนนั้น 3 ตัว เช่น '111' เป็นต้น

# Creating a dictionary from 1 to N.
# Please enter a value of n: 4
# Output = {1:'111',2:'222',3:'333',4:'444'}

print("Creating a dictionary from 1 to N.")
n = int(input("Please enter a value of n: "))
my_dict = {}

for i in range(1, n + 1):
    my_dict[i] = str(i) * 3  

print("Output =", my_dict)
