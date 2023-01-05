t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    m = {}
    for i in range(len(s)):
        m[a[i]] = s[i]
    ok = True
    for i in range(len(s)):
        if s[i] != m[a[i]]:
            ok = False
            break
    print("YES" if ok else "NO")
            
