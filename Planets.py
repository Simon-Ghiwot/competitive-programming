from collections import Counter
t = int(input())
for _ in range(t):
    n, c = input().split()
    n, c = int(n), int(c)
    l = list(map(int, input().split()))
    m = Counter(l)
    result = 0
    for key in m.keys():
        result += min(m[key], c)
    print(result)
