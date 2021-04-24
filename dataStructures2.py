#creating list from a tuple
x = list()
y = ['a', 25, 'dog', 8.34]
print(y)
tuple1 = (10,20)
print(tuple1)
z = list(tuple1)
print(z)

#list comprehensions
a = [m+1 for m in range(20) if m%2!=0]
print(a)

#delete
del(a[1])
print(a)

#append
a.append(22)
print(a)

#pop
print(a.pop())
print(a)