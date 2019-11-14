class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) -1
        indices = [*range(len(nums))]
        sorted_indices = sorted(indices, key=lambda i: nums[i])
        numss = [nums[i] for i in sorted_indices]
        while p1 < p2:
            s = numss[p1] + numss[p2]
            if s == target:
                return sorted_indices[p1], sorted_indices[p2]
            if s > target:
                p2 = p2 - 1
            if s < target:
                p1 = p1 + 1                                     
