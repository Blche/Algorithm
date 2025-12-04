T = int(input())
for i in range(1, T+1):
    Hi, Wi, Ni = map(int, input().split())
    floor = Ni % Hi
    room = Ni // Hi + 1
    if floor == 0:
        floor = Hi
        room = Ni // Hi
    print(f"{floor}{room:02d}")