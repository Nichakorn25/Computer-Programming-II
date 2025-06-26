# 2.จงเขียนโปรแกรมเพื่อแสดงจำนวนเฉพาะ (Prime number) จาก 1 ถึง N 

# Display prime number from 1 to N.
# Please enter a value of n: 40
# They are 2 3 5 7 11 13 17 19 23 29 31 37
# Total = 12


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input("Please enter a value of n: "))

prime_numbers = []
for i in range(1, n+1):
    if is_prime(i):
        prime_numbers.append(i)

print("They are", *prime_numbers)
print("Total =", len(prime_numbers))
