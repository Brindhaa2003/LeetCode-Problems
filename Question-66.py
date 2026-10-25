class solution:
    def generate(self,digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        digits.insert(0,1)
        return digits
obj=solution()
result=obj.generate([1,2,3])
print(result)

            