def MathChallenge(strParam) -> str:
    if len(strParam) == 1: return "-1"
    elif strParam[0:int(len(strParam)/2)] == strParam[int(len(strParam)/2):]: return strParam[0:int(len(strParam)/2)]
    else:
        half = int(len(strParam)/2)
        i = 0
        max = strParam[0:half-i]
        while len(max) >= 2:
            # print("Left: ", strParam[0:int(len(strParam)/2)-i], "Right: ", strParam[int(len(strParam)/2)-i:int(len(strParam)/2)-i+len(strParam[0:int(len(strParam)/2)-i])])
            if strParam[0:half-i] == strParam[half-i:half-i+len(strParam[0:half-i])]:
                return strParam[0:half-i]
            i = i + 1
            max = strParam[0:half-i]
        return "-1"
print(MathChallenge("ccababc"))
