s = input().strip()

if s == "":        # strip하고 나서 완전 빈 문자열이면
    print(0)       # 단어 0개
else:
    print(s.count(" ") + 1)
