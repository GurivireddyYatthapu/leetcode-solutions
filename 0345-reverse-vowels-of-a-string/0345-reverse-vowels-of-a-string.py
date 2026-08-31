class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'A','E','I','O','U','a','e','i','o','u'}
        left = 0
        right = n-1
        s = list(s)
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                temp = s[left]
                s[left]= s[right]
                s[right] = temp
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] not in vowels:
                right -= 1
            else:
                left += 1    
        return "".join(s)
