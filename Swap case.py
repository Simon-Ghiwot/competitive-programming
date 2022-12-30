def swap_case(s):
    ans = ""
    for i in range(len(s)):
        if s[i].isupper():
            ans += s[i].lower()
        else:
            ans += s[i].upper()
    return ans

if __name__ == '__main__':
