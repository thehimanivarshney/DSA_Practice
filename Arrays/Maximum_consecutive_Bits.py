class Solution:
    def maxConsecutiveBit(self, arr):
        max_count = 1
        count = 1
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
                
            else:
                count = 1
                
            max_count = max(max_count, count)
                
        return max_count
    
if __name__ == "__main__":
    arr = [1, 1, 1, 0, 0]
    
    obj = Solution()
    result = obj.maxConsecutiveBit(arr)
    
    print("Maximum consecutive bits:", result)