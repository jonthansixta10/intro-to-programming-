items = [ "kiwi","peach","lemon","grapes","oranges" ]

print(items[0])
print(items[-1])


items.append(input("Enter a fruit: "))

print(items)

items.remove(input("Enter a fruit to remove: "))

print(items)

items.sort()
print(items)

items1 = ["kiwi","peach","lemon","grapes","oranges","lemon" ]

items1.count("lemon")
print(items1.count("lemon"))

for item in items1:
    print(item)