class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0
        for h1, h2 in zip(heights, expected):
            if h1 != h2:
                count += 1
        return count
