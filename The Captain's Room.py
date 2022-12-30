# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room = {}
rooms = list(map(int, input().split()))
for i in range(len(rooms)):
    room[rooms[i]] = room.get(rooms[i], 0) + 1
for i in range(len(rooms)):
    if room[rooms[i]] == 1:
        print(rooms[i])
        break
