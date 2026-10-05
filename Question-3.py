class Solution:
    def generate(self,s):
        left=0
        current={}
        longest=0
        for right in range(len(s)):
            if s[right] in current and current[s[right]]>=left:
                left=current[s[right]]+1
            current[s[right]]=right
            length=right-left+1
            if length>longest:
                longest=length
        return longest
obj=Solution()
print(obj.generate("abcabcbb"))
            