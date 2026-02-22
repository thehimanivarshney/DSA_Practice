# Given an array of positive integers arr[], return the second largest element from the array. 
# If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        
        largest = float("-inf")
        second = float("-inf")
        
        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num
        
        if second == float("-inf"):
            return -1
        
        return second