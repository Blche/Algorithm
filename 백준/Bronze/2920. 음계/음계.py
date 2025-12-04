l1 = list(map(int, input().split()))
j = l1[0]
c = 0
for i in l1[1:]:
    i = int(i)
    if j < i:
        c += 1
    j = i
if c == 7:
    print("ascending")
elif c == 0:
    print("descending")
else:
    print("mixed")