class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        cur_sum  = 0
        max_sum = float('-inf')
        for right in range(len(nums)):
            cur_sum += nums[right]
            if right - left + 1 > k:
                cur_sum -= nums[left]
                left += 1
            if right -left+1 >= k:
                max_sum = max( max_sum , cur_sum)
           
        return max_sum/k

            