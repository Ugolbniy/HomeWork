class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        result = []
        for num in arr2:
            result.extend([num] * count.pop(num))
        remaining = sorted(count.items())
        for num, freq in remaining:
            result.extend([num] * freq)
        return result
