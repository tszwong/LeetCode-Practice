class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        
        for i in s:
            if i.isalnum():
                str += i
                
        if str.casefold() == str[::-1].casefold():
            return True
        
        return False
      
