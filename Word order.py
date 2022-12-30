# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = {}
words = []
for i in range(n):
    word = input()
    if word in s:
        s[word] = s.get(word) + 1
    else:
        words.append(word)
        s[word] = 1
print(len(s))
for i in range(len(words)):
    print(s.get(words[i]), end =" ")
