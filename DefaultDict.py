# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
group_a = defaultdict(list)

n, m = input().split()
n = int(n)
m = int(m)

for i in range(n):
    key = input()
    group_a[key].append(i + 1)
for i in range(m):
    key = input()
    if len(group_a[key]) == 0:
        print(-1)
    else:
        for idx in group_a[key]:
            print(idx, end = " ")
        print("")
