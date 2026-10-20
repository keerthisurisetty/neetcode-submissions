class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"]":"[", ")":"(", "}":"{"}

        for i in s:
            if i in dictionary: 
                if not stack or dictionary[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return not stack