#!/usr/bin/env python3

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]

            num_indices[num] = i

        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test case 1:", solution.twoSum(nums1, target1))  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("Test case 2:", solution.twoSum(nums2, target2))  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("Test case 3:", solution.twoSum(nums3, target3))  # Expected: [0, 1]
