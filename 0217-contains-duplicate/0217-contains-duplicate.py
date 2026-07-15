class Solution(object):
    def containsDuplicate(self, nums):
        T=set()
        for num in nums :
            if num in T:
                return True 
            T.add(num)
        return False 

        