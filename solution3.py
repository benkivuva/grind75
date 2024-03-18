#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

# Test cases
if __name__ == "__main__":
    # Test case 1
    list1_1 = ListNode(1)
    list1_2 = ListNode(2)
    list1_3 = ListNode(4)
    list1_1.next = list1_2
    list1_2.next = list1_3

    list2_1 = ListNode(1)
    list2_2 = ListNode(3)
    list2_3 = ListNode(4)
    list2_1.next = list2_2
    list2_2.next = list2_3

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1_1, list2_1)

    print("Test case 1:", end=" ")
    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next
    print()

    # Test case 2
    list1_1 = None
    list2_1 = None

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1_1, list2_1)

    print("Test case 2:", end=" ")
    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next
    print()

    # Test case 3
    list1_1 = None
    list2_1 = ListNode(0)

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1_1, list2_1)

    print("Test case 3:", end=" ")
    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next
    print()