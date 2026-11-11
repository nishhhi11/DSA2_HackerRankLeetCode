a = [5, 10, 15]
b = a
c = a.copy()

b.append(20)
c.append(25)

print(a)
print(b)
print(c)

print(a is b)
print(a is c)
print(a == c)