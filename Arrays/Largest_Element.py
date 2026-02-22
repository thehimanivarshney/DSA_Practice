#Given an array arr[]. 
# The task is to find the largest element and return it.

class Solution:
    def largest(self, arr):
        if not arr:
            return None
            
        largest = arr[0]
        
        for i in range(1, len(arr)):
                if(arr[i]>largest):
                    largest=arr[i]
            
        return largest