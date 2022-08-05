n = int(input('Enter number of items:'))
items = []
while n > 0:
    item = input('Enter item :')
    items.append(item)
    n = n - 1

numbers = '0123456789'
for item in items:
    f = True
    for i in item:
        if not i in numbers:
            f = False
            break
    if f:
        print(item)
