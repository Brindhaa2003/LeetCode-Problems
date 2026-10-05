
class Solution:
    def generatePara(self,n):
        result=[]
        def generate(current,open,close):
            if len(current)==2*n:
                result.append(current)
                return
            if close < open:
                generate(current+")",open,close+1)
            if open < n:
                generate(current+"(",open+1,close)
        generate("",0,0)
        return result
obj=Solution()
result=obj.generatePara(3)
print(result)