class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        lon = 1
        cur = 1
        if not nums:
            return 0
        
        for i in range(len(nums)-1):
            
            if nums[i] + 1 == nums[i+1]:
                cur+=1
                continue
            elif nums[i]==nums[i+1]:
                continue
            else:
                lon = max(lon, cur)
                cur = 1
        lon = max(lon, cur)   
        return lon
                
            