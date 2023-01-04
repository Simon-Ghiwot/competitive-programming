import textwrap

def wrap(string, max_width):
    i = 0
    result = ""
    while i < len(string):
        current = string[i : min(i + max_width, len(string))]
        result += current + "\n"
        i += max_width
        
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
