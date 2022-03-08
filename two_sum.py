class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        n=len(nums)

        while i<n-1:
            j=i+1
            while j<n:
                s=nums[i]+nums[j]
                if s==target:
                    return [i,j]
                j=j+1
            i=i+1