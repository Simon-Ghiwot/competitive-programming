# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = 0
for i in range(len(arr)):
    if arr[i] in a:
        ans += 1
    if arr[i] in b:
        ans -= 1
print(ans)
