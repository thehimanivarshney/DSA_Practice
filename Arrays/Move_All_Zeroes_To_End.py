# Move All Zeroes to End

# You are given an array arr[] of non-negative integers. 
# You have to move all the zeros in the array to the right end while 
# maintaining the relative order of the non-zero elements. 
# The operation must be performed in place,
# meaning you should not use extra space for another array.

class Solution:
    def pushZerosToEnd(self, arr):
        n= len(arr)
        i = 0
        for j in range(n):
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        return arr
    
if __name__ == "__main__":
    arr = [1, 0, 2, 0, 4]
    obj = Solution()
    print(obj.pushZerosToEnd(arr))