class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 你的代码
        k=1
        for num in nums:
            if num!=nums[k-1]:
                nums[k]=num
                k+=1
        nums[k:].clear()
        return k

        