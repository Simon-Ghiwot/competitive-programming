# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
english = set(map(int, input().split()))
n = input()
french = set(map(int, input().split()))
print(len(english.union(french)))
