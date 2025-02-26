user_input = input("Enter a string: ")
print("You entered:", user_input)

if user_input == "":
    print("Please enter a non-empty string.")
    user_input = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for i in user_input:
    if i in vowels:
        count += 1
print("The number of vowels in", user_input,"is",count)
