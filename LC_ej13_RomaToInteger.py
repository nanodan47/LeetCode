"""
En internet encontré que había una pista de que era más fácil empezar de atrás hacia adelante. 
La primera solución es mejor que la segunda.

Link Solution 1: https://www.youtube.com/watch?v=zCqaFVYoPBw&ab_channel=TimothyHChang
"""
class Solution:
    def romanToInt(s: str) -> int:
        s = s.upper()
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        number = 0
        L = len(s)
        i= L-1
        while i>=0:
            if(i<L-1) and romans[s[i]]<romans[s[i+1]]:
                number -= romans[s[i]]
            else:
                number += romans[s[i]]
            i-=1
        return number
    s = "MCMXCIV"
    print(romanToInt(s))
    
class Solution:
    def romanToInt(s: str) -> int:
        s = s.upper()
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        number = 0
        i=0
        while i < len(s):
            if (i+1 < len(s)) and (s[i:i+2] in romans):
                number+= romans[s[i:i+2]]
                i+=2
            else:
                number+=romans[s[i]]
                i+=1
        return number

    s = "MCMXCIV"
    print(romanToInt(s))