a = input()
H, M = map(int, a.split())

if M >= 45 :
    M = M - 45
else :
    if H == 0 :
        H = 23
        M = M + 15
    else :
        H = H -1
        M = M + 15
print(H, M)