class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i in range(len(nums)-k+1):
            w = nums[i:i+k]
            m = max(w)
            s.append(m)
            
        return (s)

