#Given an integer x, return true if x is a palindrome,and false otherwise.
#Input: x = 121; Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x = x // 10
        return original == reversed_num
   # Test the function
solution = Solution()
print(solution.isPalindrome(101))  # Example input 1
print(solution.isPalindrome(-121))  # Example input 2
print(solution.isPalindrome(10))  # Example input 3
