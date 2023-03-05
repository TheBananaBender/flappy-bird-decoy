class Solution:
    def prod(lst):
        prod = 1
        for i in range(len(lst)):
            prod *= lst[i]
        return prod
    def maximumProduct(self, nums: list[int], k: int):
        i = 0
        return max(Solution.prod(nums),Solution.maximumProdRec(self, nums,k-1, i)) % (10**9 + 7)
    def maximumProdRec(self,nums,k,i):
        if i == len(nums):
            return(Solution.prod(nums))
        prod = Solution.prod(nums)
        nums[i] += 1
        if k == 0:
            return(Solution.prod(nums))
        if i == len(nums) - 1:
            x = Solution.maximumProdRec(self, nums,k-1, i)
            return max([x,prod])
        x = Solution.maximumProdRec(self, nums,k-1, i)
        nums[i] -= 1
        nums[i+1] +=1
        y = Solution.maximumProdRec(self, nums, k - 1, i + 1)
        nums[i+1] -= 1
        return max([x,y,prod])
sol = Solution()
print(sol.maximumProduct([0,4],5))