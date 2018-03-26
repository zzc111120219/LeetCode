class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 1 if x > 0 else -1
        r = s * int(str(s*x)[::-1])
        return r if r.bit_length() < 32 else 0
        
        
if __name__ == '__main__':
    test = Solution()
    result = test.reverse(123331)
    print(result)
