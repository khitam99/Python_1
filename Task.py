#Example 1
row_num=input("Enter the number of rows: ")
if row_num.isdigit():
    row=int(row_num)
    for i in range(1, row+1):
        for j in range(1, i + 1):
            print(j,end='')
        print()
    print("Example 1 is Done!! ")
else:
    print("Invalid input! Please enter a valid number.")
print()

#Example 2
row_num=input("Enter the number of rows: ")
if row_num.isdigit():
    row=int(row_num)
    a="*"
    for i in range(1, row+1):
        for j in range(1, i + 1):
            print(a,end='')
        print()
    print("Example 2 is Done!! ")
else:
    print("Invalid input! Please enter a valid number.")
print()

#Example 3
row_num=input("Enter the number of rows: ")
if row_num.isdigit():
    row=int(row_num)
    a="*"
    for i in range(row):
        print(" "*(row-1-i)+a*(2*i+1))  

    print("Example 3 is Done!!")
else:
    print("Invalid input! Please enter a valid number.")
print()