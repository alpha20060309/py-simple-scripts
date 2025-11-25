from typing import List

Nums = [1,2,3,5, 6, 7]
Target = 13
num_dict = {1 :0, 2:1, 3:2, 5:3, 6:4, 7:5}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f"Starting twoSum with nums: {nums}, target: {target}")
        num_dict = {}

        for i, num in enumerate(nums):
            print(f"Processing index {i}, value {num}")
            complement = target - num
            print(f"Looking for complement: {complement}")

            if complement in num_dict:
                print(f"Found complement {complement} at index {num_dict[complement]}")
                result = [num_dict[complement], i]
                print(f"Returning result: {result}")
                return result
    
            num_dict[num] = i
            print(f"Added {num} at index {i} to dictionary")
            print(f"Current dictionary: {num_dict}")

        print("No two sum solution found, returning empty list")
        return []


# print(Solution().twoSum(Nums, Target))

