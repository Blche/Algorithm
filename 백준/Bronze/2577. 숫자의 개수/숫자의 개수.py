a = int(input())
b = int(input())
c = int(input())
m = str(a * b * c)
for i in range(10):
    print(m.count(str(i)))