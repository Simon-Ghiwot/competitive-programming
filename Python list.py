if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        commands = input().split(' ')
        if commands[0] == 'print':
            print(nums)
        elif commands[0] == 'insert':
            nums.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == 'append':
            nums.append(int(commands[1]))
        elif commands[0] == 'sort':
            nums.sort()
        elif commands[0] == 'remove':
            nums.remove(int(commands[1]))
        elif commands[0] == 'pop':
            nums.pop()
        elif commands[0] == 'reverse':
            nums.reverse()
