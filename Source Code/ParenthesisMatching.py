class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackList = []
        for ch in s :
            if ch == '(' or ch == '{' or ch == '[' :
                stackList.append(ch)
            if(ch == ')' or ch == '}' or ch == ']'):
                if len(stackList) == 0 :
                    return False
                char_pop = stackList.pop()
                if not((char_pop == '(' and ch == ')') or (char_pop == '{' and ch == '}') or (char_pop == '[' and ch==']')) :
                    return False
        if(len(stackList) != 0) :
            return False
        return True