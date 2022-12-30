# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())
for i in range(test):
    size = int(input())
    nums = list(map(int, input().split(" ")))
    left, right = 0, size - 1
    prev = min(nums[left], nums[right])
    ok = True
    while left <= right:
        minimum = min(nums[left], nums[right])
        if minimum < prev:
            ok = False
            break
        if nums[left] < nums[right]:
            left += 1
            prev = nums[left]
        else:
            right -= 1
            prev = nums[right]
    print("Yes" if ok else "No")
    test -= 1
