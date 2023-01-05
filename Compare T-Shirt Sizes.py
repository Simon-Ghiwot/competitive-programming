m = {"S" : 1, "M" : 2, "L" : 3}
t = int(input())
for _ in range(t):
    s, t = input().split()
    i, j = 0, 0
    while s[i] == "X":
        i += 1
    while t[j] == "X":
        j += 1
    if s[i] == t[j]:
        if len(s) > len(t) and s[i] == "S" or len(s) < len(t) and s[i] == "L":
            print("<")
        elif len(s) < len(t) and s[i] == "S" or len(s) > len(t) and s[i] == "L":
            print(">")
        else:
            print("=")
    elif m[s[i]] > m[t[j]]:
        print(">")
    else:
        print("<")
