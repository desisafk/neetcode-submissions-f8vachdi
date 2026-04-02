class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        for char in s:
            list.append(char)
        if len(s) == len(t):
            for char in t:
                if char in list:
                    list.remove(char)
                elif char not in list:
                    return False
            if not list:
                return True
        else:
            return False