def romanToInt(s: str) -> int:
    chardict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    marker = 0
    while marker < len(s) - 1 :
        print(" Marker: " + str(marker) + "   Result: " + str(result) + "   " )
        if chardict[s[marker]] < chardict[s[marker+1]]:
            result+=(chardict[s[marker+1]] - chardict[s[marker]])
            marker+=2
        result+=chardict[s[marker]]
        marker+=1
    result+=chardict[s[marker]]
    return result

test = "MCMXCIV"
print(romanToInt(test))