from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()

        for n in nums:
            if n in counts:
                return True
            
            counts.add(n)

        return False

if __name__ == "__main__":
    s = Solution()

    print("-"*50)
    print("Running test cases for Contains Duplicate")

    test_case_1 = [1, 1]
    assert s.hasDuplicate(test_case_1) == True, f"Test case {test_case_1} failed"

    test_case_2 = [1, 2]
    assert s.hasDuplicate(test_case_2) == False, f"Test case {test_case_2} failed"

    print("All test cases passed!")
    print("-"*50)