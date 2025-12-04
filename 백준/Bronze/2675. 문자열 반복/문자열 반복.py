T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    pt = ""
    for i in S:
        pt = pt + i*R
    print(pt)