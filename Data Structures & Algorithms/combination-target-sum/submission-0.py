class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def backtrack(i, target):
            if target == 0 :
                res.append(sub.copy())
                return 
            if target<0:
                return

            for j in range(i,len(nums)):
                sub.append(nums[j])
                backtrack(j,target - nums[j])
                sub.pop()
        backtrack(0, target)
        return res

