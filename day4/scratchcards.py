nums = []
nums2 = []
input = open('day4/input.txt', 'rt')
for line in input:
    nums, nums2 = line.rstrip().split('|')
    

for i, item in enumerate(nums):
    for j, num in enumerate(item):
        if num == '':
            item.pop(j)

    nums[i] = item[2:]
    tempFirstNums = nums[i][10:]
    tempSecondNums = nums[i][:25]
    if tempSecondNums in tempFirstNums:
        print('here')