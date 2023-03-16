def MathChallenge(strParam) -> str:
    if len(strParam) == 1: return "-1"
    elif strParam[0:int(len(strParam)/2)] == strParam[int(len(strParam)/2):]: return strParam[0:int(len(strParam)/2)]
    else:
        i = 0
        max = strParam[0:int(len(strParam)/2)-i]
        while len(max) >= 2:
            print("Left: ", strParam[0:int(len(strParam)/2)-i], "Right: ", strParam[int(len(strParam)/2)-i:int(len(strParam)/2)-i+len(strParam[0:int(len(strParam)/2)-i])])
            if strParam[0:int(len(strParam)/2)-i] == strParam[int(len(strParam)/2)-i:int(len(strParam)/2)-i+len(strParam[0:int(len(strParam)/2)-i])]:
                return strParam[0:int(len(strParam)/2)-i]
            i = i + 1
            max = strParam[0:int(len(strParam)/2)-i]
        return "-1"
print(MathChallenge("abcababcababcab"))
