num = [20,50,30,40,80]
print(num)
num.sort()
print(num[-2])

# name = "racecar"
name = str(input("Enter name: "))
reverse = name[::-1]

print("Reversed:", reverse)

if name == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")