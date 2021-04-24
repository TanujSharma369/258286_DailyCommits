x = "computer"

#omp
print(x[1:4])
#opt
print(x[1:6:2])
#com
print(x[:3])
#comput
print(x[:-2])

x = 'horse ' + 'shoe'
print(x)

z = ('abc', 'def', 'ghi') + ('jkl',)
print(z)

# testing membership

str = 'bug'
#True
print('u' in str)

#enumerate
a = [7,8,9,-10]
for index, item in enumerate(a):
    print(index , item)

animals = ['cat', 'cheetah', 'camel', 'catfish', 'caterpillar']
print(min(animals))

#sorting according to second character
print(sorted(animals, key=lambda k: k[1]))

print(animals.count('cat'))


