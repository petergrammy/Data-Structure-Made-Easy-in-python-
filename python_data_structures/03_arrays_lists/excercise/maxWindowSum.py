def maxWindowSum(nums, k):
    left = 0
    right = k

    current_sum = sum(nums[:k])
    max_sum = current_sum

    while right < len(nums):

        # 这里两行你来写：
        # 1. 删除离开窗口的数字
        current_sum-=nums[left]
        # 2. 加入进入窗口的数字
        current_sum+=nums[right]
        max_sum = max(max_sum, current_sum)

        left += 1
        right += 1

    return max_sum