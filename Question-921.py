class solution:
    def generate(self,s):
        open_count=0
        close_count=0
        for i in s:
            if i=="(":
                open_count+=1
            else:
                if open_count>0:
                    open_count-=1
                else:
                    add_count+=1
        return open_count+add_count
obj=solution()
result=obj.generate("()))((()))")
print(result)