# Rotate Array by One
# Given an array arr, 
# rotate the array by one position in clockwise direction.

class Solution:
    def rotate(self, arr):
        
        n = len(arr)
        if n <= 1:
            return arr
            
        temp = arr[n-1]
            
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i -1]
        
        arr[0] = temp
            
        return arr