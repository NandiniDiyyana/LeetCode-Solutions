class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        max_inc, max_dec = 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc += 1
                max_inc = max(inc, max_inc)
            else:
                inc = 1
            if nums[i] > nums[i+1]:
                dec += 1
                max_dec = max(dec, max_dec)
            else:
                dec = 1
        return max(max_inc, max_dec)

        
        