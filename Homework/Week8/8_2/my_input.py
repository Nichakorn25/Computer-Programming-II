def get(min_val, max_val):
    while True:
        num = int(input(f"Enter a number ({min_val}–{max_val}): "))
        if min_val <= num <= max_val:
            print(f"You entered number {num}")
            break
        else:
            print("Invalid Input!!!")
