class solution:
    def generate(self,s):
        stack=[0]
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                value=stack.pop()
                if value==0:
                    value=1
                else:
                    value=2*value
                stack[-1]=stack[-1]+value
        return stack[0]
obj=solution()
result=obj.generate("(()()())")
print(result)

