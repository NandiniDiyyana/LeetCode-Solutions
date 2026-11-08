class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        mini = min(nums)
        maxi = max(nums)
        return max(0, (maxi - mini) - 2 * k)
        