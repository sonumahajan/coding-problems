class Solution:
    def isPalindrome(self, num0: int) -> bool:
        num = num0
        result = 0
        if num0 >= 0:
            while(num != 0):
                temp = num % 10
                result = result * 10 + temp
                num = num // 10
            if(num0 == result):
                return True
            else:
                return False
        else:
            return False

obj = Solution()
print(obj.isPalindrome(121)) # True
print(obj.isPalindrome(-121)) # False
print(obj.isPalindrome(10)) # False

