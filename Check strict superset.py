# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split(' '))
n = int(input())
answer = True

for _ in range(n):
     t = set(input().split(' '))
     if not a.issuperset(t):
        answer = False 
        break
print(answer)  
