""" 79.26% faster 48ms"""
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
   inhash={}
   for i in range(len(nums)):
     sub = target - nums[i] #difference
     if sub in inhash:
         return [inhash[su],i] # if present return
     inhash[nums[i]] = i


""" We solve this problem using dictionary in python.
Where we do not caluclate the difference between the target and current value and store the index as value and difference as key in dictionary,
if the difference  is already present in the dictionary we return the current index and the value of the difference. 
Which ultimatley is the index.
""
