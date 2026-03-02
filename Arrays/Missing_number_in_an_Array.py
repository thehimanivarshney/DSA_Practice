class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        xor1 = 0
        xor2 = 0
        
        # XOR from 1 to n
        for i in range(1, n + 1):
            xor1 ^= i
        
        # XOR all elements of array
        for num in arr:
            xor2 ^= num
        
        return xor1 ^ xor2
    
if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    
    obj = Solution()
    result = obj.missingNum(arr)
    
    print("Missing number is:", result)