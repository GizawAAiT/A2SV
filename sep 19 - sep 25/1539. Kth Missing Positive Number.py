class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k > (arr[-1]-len(arr)):
            return k + len(arr)
        
        i, j = -1, len(arr)
        while i < j-1:
            m = (i+j)//2
            if arr[m] - (m+1) >= k:
                j = m
            else:
                i = m
        return k if i == -1 else k + i + 1
     