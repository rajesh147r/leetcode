class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isalnum():              # Only keep alphabets
                result += char.lower()      # Convert to lowercase
        return result == result[::-1]       # Check palindrome
