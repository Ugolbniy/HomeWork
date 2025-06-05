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

if __name__ == "__main__":
    sol = Solution()
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(sol.relativeSortArray(arr1, arr2))
