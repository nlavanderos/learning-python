from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        signo=False
        if(type(target)!=int) :
            return 0

        signo=False
        #nums.sort()
        i=0
        j=1
        while(signo!=True):
            
            if(nums[i]+nums[j] ==target):
                signo=True

            else:
                if(j<len(nums)-1):
                    j+=1
                
                elif(j==len(nums)-1):
                    i+=1
                    j=i+1

        return [i,j]


target=6
nums=[3,2,4]

objeto=Solution()
print(objeto.twoSum(nums,target))