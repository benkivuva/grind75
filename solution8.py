#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        for count in char_count.values():
            if count != 0:
                return False
        
        return True

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1, t1 = "anagram", "nagaram"
    solution = Solution()
    print("Test case 1:", solution.isAnagram(s1, t1))  # Expected: True

    # Test case 2
    s2, t2 = "rat", "car"
    print("Test case 2:", solution.isAnagram(s2, t2))  # Expected: False
