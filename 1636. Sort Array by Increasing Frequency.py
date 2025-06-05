from collections import Counter

class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,2,2,3]
    print(sol.frequencySort(nums))
