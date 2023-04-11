from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        run_test_case()

def run_test_case():
    MAX = pow(2, 32)
    l = I()
    result, stack = 0, [1]
    for i in range(l):
        arg = input().split()
        if len(arg) == 1:
            if arg[0] == "add":
                if stack:
                    result += stack[-1]
            else:
                stack.pop()
        else:
            current = int(arg[-1]) * stack[-1]
            stack.append(min(current, MAX))
    if result >= MAX:
        print("OVERFLOW!!!")
    else:
        print(result)
if __name__ == "__main__":
    main()

