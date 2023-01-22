class Solution(object):
    def isValid(self, s):
        list = []
        if len(s) == 1: return False
        for e in s:
            if not list and e in (')', '}', ']'): return False
            if e == '(' or e == '{' or e == '[':
                list.append(e)
            elif list:
                if e == ')':
                    if list and list.pop() != '(':
                        return False
                elif e == '}':
                    if list and list.pop() != '{':
                        return False
                elif e == ']':
                    if list and list.pop() != '[':
                        return False        
        if list:
            return False
        else:
            return True
            
