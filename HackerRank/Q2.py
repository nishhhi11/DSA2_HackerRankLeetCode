def simpleArraySum(ar):
    return sum(ar)

n = int(input("Enter number of elements: "))
ar = list(map(int, input("Enter the numbers: ").split()))

result = simpleArraySum(ar)
print(result)