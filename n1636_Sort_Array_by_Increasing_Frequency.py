from collections import Counter

class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
