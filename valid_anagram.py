class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # keep track of letters in both strings
        d1 = {}
        d2 = {}

        # iterate to update tracker
        for i in range(len(s)):
            # checking s
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1

            # checking t
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1

        # check if number of letters 
        for i in d1:
            if i in d1 and i not in d2:
                return False
            # letter appears in both but different amount of times
            elif i in d1 and i in d2 and d1[i] != d2[i]:
                return False

        return True
