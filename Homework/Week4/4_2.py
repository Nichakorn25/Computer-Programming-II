# จงเขีนโปรแกรมในการกำหนดตัวแปรดังต่อไปนี้ี
# n = [7, 2, 4, 1, 5, 9, 3]
# str = 'ratchasima'
# animal = ('dog', 'cat', 'snake', 'rabbit')
# product = {'ruler': 5, 'box': 12, 'book': 9}
# แล้วใช้ฟังก์ชันสำเร็จรูปต่างๆเพื่อให้ได้ผลลัพธ์ ดังแสดงในตัวอย่างการรันโปรแกรม

# Biggest number in n is 9
# Smallest number in n is 1
# Sum of all numbers in n is 31
# Total number in n is 7
# Biggest character in str is t
# Smallest character in str is a
# Total character in str is 10
# Original str = ratchasima
# Sorted str = ['a', 'a', 'a', 'c', 'h', 'i', 'm', 'r', 's', 't']
# Descending order str = ['t', 's', 'r', 'm', 'i', 'h', 'c', 'a', 'a', 'a']
# Original animal = ('dog', 'cat', 'snake', 'rabbit')
# Sorted animal = ['cat', 'dog', 'rabbit', 'snake']
# Original product = {'ruler': 5, 'box': 12, 'book': 9}
# Sorted product = ['book', 'box', 'ruler']



n = [7, 2, 4, 1, 5, 9, 3]
str_val = 'ratchasima'
animal = ('dog', 'cat', 'snake', 'rabbit')
product = {'ruler': 5, 'box': 12, 'book': 9}


print("Biggest number in n is", max(n))
print("Smallest number in n is", min(n))
print("Sum of all numbers in n is", sum(n))
print("Total number in n is", len(n))

print("Biggest character in str is", max(str_val))
print("Smallest character in str is", min(str_val))
print("Total character in str is", len(str_val))
print("Original str =", str_val)

sorted_str = sorted(str_val)
print("Sorted str =", sorted_str)

desc_str = sorted(str_val, reverse=True)
print("Descending order str =", desc_str)

print("Original animal =", animal)
sorted_animal = sorted(animal)
print("Sorted animal =", sorted_animal)

print("Original product =", product)

sorted_product = sorted(product, key=product.get)
sorted_product.reverse()
print("Sorted product =", sorted_product)  # ได้ ['box', 'book', 'ruler']
