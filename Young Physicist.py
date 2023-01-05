t = int(input())
x, y, z = 0, 0, 0
for i in range(t):
    cur = list(map(int, input().split()))
    x += cur[0]
    y += cur[1]
    z += cur[1]
print("YES" if not x and not y and not z else "NO")
