list = []
x = 1
while x <= 3:
    list.append(eval(input()))
    x = x+1
list1 = list.copy()
list.sort()
for b in list:
    print(b)
print()
for b in list1:
    print(b)
