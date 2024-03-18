#!/usr/bin/env python3

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        return not stack

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "()"
    print("Test case 1:", solution.isValid(s1))  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print("Test case 2:", solution.isValid(s2))  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print("Test case 3:", solution.isValid(s3))  # Expected: False
    
    # Test case 4
    s4 = "([)]"
    print("Test case 4:", solution.isValid(s4))  # Expected: False
    
    # Test case 5
    s5 = "{[]}"
    print("Test case 5:", solution.isValid(s5))  # Expected: True