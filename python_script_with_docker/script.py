print('Starting script.')

a = {1: 2, 3: 4, 'foo': 'bar'}
b = {}

for k, v in reversed(list(a.items())):
    b.update({v: k})

print(b)
