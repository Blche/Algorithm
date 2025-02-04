n = int(input())
a = 0
while a < n:
    a = a + 1
    stars = "*"*a
    right = stars.rjust(n)
    print(right)