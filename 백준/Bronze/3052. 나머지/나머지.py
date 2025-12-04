setA = set()
for _ in range(10):
    a = int(input())
    setA.add(a % 42)
print(len(setA))