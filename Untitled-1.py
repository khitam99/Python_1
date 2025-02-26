
num = input("Enter a number: ")
if not num.isdigit():
    print("Invalid input. Please enter a valid number.")
    num = input("Enter a number: ")

num = int(num)


specific_range = input("Enter the range for the table: ")
if not specific_range.isdigit():
    print("Invalid input. Please enter a valid range.")
    specific_range = input("Enter the range for the table: ")


specific_range = int(specific_range)


for i in range(1, specific_range + 1):
    print(num, "x", i, "=", num * i)
