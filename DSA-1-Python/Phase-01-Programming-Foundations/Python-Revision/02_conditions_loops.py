a = int(input("Enter a number: "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(1, a + 1):
    print(i)

i = 1

while i <= a:
    print(i)
    i += 1

i = 1
total = 0

while i <= a:
    total += i
    i += 1

print("Sum:", total)