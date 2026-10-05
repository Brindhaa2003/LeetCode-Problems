class Solution:
    def generate(self,n):
        result=[]
        stack=[("",0,0)]
        while stack:
            current,open,close=stack.pop()
            if len(current)==2*n:
                result.append(current)
            if close < open:
                stack.append((current+")",open,close+1))
            if open < n:
                stack.append((current+"(",open+1,close))
        return result
obj=Solution()
print(obj.generate(3))