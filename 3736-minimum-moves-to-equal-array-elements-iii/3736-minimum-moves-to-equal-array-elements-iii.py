class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = 0
        for i in range(len(nums)):
            count += max_num - nums[i]
        return count
            
        