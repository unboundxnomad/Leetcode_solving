class Solution(object):
    def containsDuplicate(self, nums):
        t=set()
        for num in nums:
            if num in t:
                return True 
            t.add(num)
        return False  

    
        
        