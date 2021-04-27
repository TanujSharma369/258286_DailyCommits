under_10 = [x for x in range(10)]
print('under_10:' +str(under_10))

squares = [x*x for x in under_10]
print('squares:' +str(squares))

odds = [x for x in range(10) if x%2==1]
print('odds:' +str(odds))

sentence = 'I love 2 go t0 the store 7 times a w3ek'
nums = [x for x in sentence if x.isnumeric()]
print('nums:' + ''.join(nums))

names = [ 'Nishant', 'Pankaj', 'Santosh', 'Tanuj','Abdul']
index = [k for k, v in enumerate(names) if v == 'Tanuj']
print('index :' +str(index[0]))

letters = [x for x in 'ABCDEFGHI']
letters = [a for a in letters if a!='C']
print('letters:'+str(letters))