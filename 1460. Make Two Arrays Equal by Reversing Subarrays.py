class Solution:
    def canBeEqual(self, target, arr):
        return sorted(target) == sorted(arr)

if __name__ == "__main__":
    sol = Solution()
    target = [1,2,3,4]
    arr = [2,4,1,3]
    print(sol.canBeEqual(target, arr))
