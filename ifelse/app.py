a = 10
b = 3

if a > b:
    print(a, 'is bigger than', b)
# 10 is bigger than 3

if b > a:
    print(b, 'is bigger than', a)
else:
    print(b, 'is lower than', a)
# 3 is lower than 10

if b > a:
    print(b, 'is bigger than', a)
elif b < a:
    print(b, 'is lower than', a)
    # 3 is lower than 10

if b > a:
    print(b, 'is bigger than', a)
elif b == a:
    print(b, 'is equal', a)
else:
    print(b, 'is not bigger nor equal', a)
# 3 is not bigger nor equal 10


if b > a:
    print(b, 'is bigger than', a)
elif b == a:
    print(b, 'is equal', a)
elif b != a:
    print(b, 'is different from', a)
else:
    print(b, 'is not bigger nor equal', a)
# 3 is different from 10
