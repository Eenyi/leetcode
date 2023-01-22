class Solution(object):
    def longestCommonPrefix(self, strs):
        minLen = sys.maxint
        result = ""
        for e in strs:
            if len(e) < minLen:
                minLen = len(e)
        for i in range(0, minLen):
            previous = strs[0][i]
            for e in strs:
                if e[i] != previous:
                    if result is None: 
                        return ""
                    else:
                        return result
            result = result + previous
        return result
# just wanted to check if commits work now or not ??