l1 = []
count = 0
while count < 9:
    a = int(input())
    l1.append(a)
    count += 1
m = max(l1)
print(m)
print(l1.index(m)+1)