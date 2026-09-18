class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 你的代码
        
        k=0
        for num in nums:
            if num!=val:
                nums[k]=num
                k+=1

        return k
