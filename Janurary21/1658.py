    def minOperations(self, nums: List[int], x: int) -> int:
        target, size, win_sum, lo, n = sum(nums) - x, -1, 0, -1, len(nums)
        for hi, num in enumerate(nums):
            win_sum += num
            while lo + 1< n and win_sum > target:
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target:
                size = max(size, hi - lo)
        return -1 if size < 0 else n - size
