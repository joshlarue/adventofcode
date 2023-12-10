nums = []
input = open('day4/input.txt', 'rt')
for line in input:
    nums.append(line.rstrip().split(' '))

for i, item in enumerate(nums):
    for iter, num in enumerate(item):
        if num == '' or num == '|':
            item.pop(iter)
    nums[i] = item[2:]

print(nums)