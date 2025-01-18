a = map(int,input().split())
aa = (i*i for i in a)
print(sum(aa) % 10)