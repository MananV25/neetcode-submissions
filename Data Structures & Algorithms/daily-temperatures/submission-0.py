class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        
        for t in range(len(temperatures)):
            while stack and temperatures[t]>temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev]= t - prev
            
            stack.append(t)
                
        return ans
