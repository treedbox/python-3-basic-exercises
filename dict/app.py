"""Dict is an object with key and value unique key: value."""

dic = {
    'foo': 15,
    'bar': 20,
    'foo': 16,  # overhide previow declaration
    'bar': 22,
    'joni': 'Treedbox'
}

print(dic)
# {'foo': 15, 'bar': 20, 'joni': 'Treedbox'}

print(dic['joni'])
# Treedbox

# add to dict

dic['answer'] = 42
print(dic)
# {'foo': 15, 'bar': 20, 'joni': 'Treedbox', 'answer': 42}

# add key value in dict

dic['answer'] = 32
print(dic)
# {'foo': 15, 'bar': 20, 'joni': 'Treedbox', 'answer': 32}

# remove key value from dict

del dic['joni']
print(dic)
# {'foo': 15, 'bar': 20, 'answer': 32}

dic['goo'] = ['A', 'B']
print(dic['goo'][1])
# B
print(dic['goo'][0])
# A

dic['goo'][0] = 'C'
print(dic['goo'][0])
# C

print(dic)
{'foo': 15, 'bar': 20, 'answer': 32, 'goo': ['C', 'B']}
