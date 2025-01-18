a = map(int,input().split())
aa = [num**2 for num in a]
print(sum(aa) % 10)