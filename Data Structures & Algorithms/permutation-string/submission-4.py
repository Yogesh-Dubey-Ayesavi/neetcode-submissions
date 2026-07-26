class Solution:


    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        need = self.buildCountMap(s1)
        windowMap = {}

        for right in range(0, len(s2)):
            
            windowMap[s2[right]] = windowMap.get(s2[right],0)+1
            if right - left + 1 > len(s1):
                windowMap[s2[left]]-=1
                if windowMap[s2[left]]==0:
                    del windowMap[s2[left]]
                left+=1
            
            if windowMap == need:
                return True
            
        return False




    
    def buildCountMap(self, s:str):
        m = {}
        for i in s:
            m[i] = m.get(i,0)+1
        return m

# Pseudo code
'''

'''


#lecacabee