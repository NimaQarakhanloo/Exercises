n = int(input())
items = []
while n > 0:
    item = input()
    items.append(item)
    n = n - 1

print(items)
items_set = set(items)
while len(items_set) > 0:
    x = items_set.pop()
    c = 0
    for item in items:
        if item == x:
            c = c + 1
    print('{} >> {}'.format(x,c))
    
