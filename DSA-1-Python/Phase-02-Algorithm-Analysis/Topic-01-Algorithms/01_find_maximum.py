#This algorithm is called Linear Traversal to Find Maximum.
#time complexity O(n)
#space complexity O(1)

numbers = [12, 35, 8, 50, 21]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number:", largest)