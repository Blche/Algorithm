T = int(input())
for _ in range(T):
    a = input()
    c = 0
    sum = 0
    for i in a:
        if i == "X":
            c = 0
        else:
            c += 1
            sum += c
    print(sum)