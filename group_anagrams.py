class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        res = []

        # sort the characters in string in alphabetic order
        for i in range(len(strs)):
            sorted_chars = sorted(strs[i]) # sort
            word = ''.join(sorted_chars) # joined the characters back together

            # check if the sorted version of word in dict
            if word not in a: 
                a[word] = [strs[i]] # new entry
            else:
                a[word].append(strs[i])

        for item in a:
            res.append(a[item])        

        return res
