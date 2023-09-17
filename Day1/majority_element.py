"""
        Find the majority element in the given list of integers using Moore's Voting Algorithm.
        
        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The majority element if it exists, otherwise -1.
"""


class Solution:
    def majorityElement(self, nums):
        # Initialize variables for counting and storing the majority element.
        count = 0  # Count of the current candidate majority element.
        candidate = None  # Current candidate majority element.

        # Applying Moore's Voting Algorithm:
        for num in nums:
            if count == 0:
                # If count is 0, set the current element as the candidate.
                candidate = num
                count = 1
            elif candidate == num:
                # If the current element matches the candidate, increment the count.
                count += 1
            else:
                # If the current element is different, decrement the count.
                count -= 1

        # Verify if the candidate is indeed the majority element by counting its occurrences.
        count_candidate = nums.count(candidate)

        if count_candidate > (len(nums) // 2):
            return candidate
        else:
            return -1

        ##better solution (slow)
        # return sorted(nums)[len(nums)//2]
