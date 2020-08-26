#https://leetcode.com/discuss/interview-question/356960


def pair(nums, target):
    to_check, li = target - 30, []
    di, me = {}, -1
    for i in range(len(nums)):
        if nums[i] not in di:
            di[to_check - nums[i]] = i
        else:
            if to_check - nums[i] > me or nums[i] > me:
                li[0] = di[nums[i]]
                li[1] = i
                me = max(nums[i], to_check - nums[i])
    return li


nums = [0, 0, 0]
print(pair(nums, 90))
