class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}'for s in strs)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        l = 0
        while i < len(s):
            ch = s[i]
            if ch == '#':
                    length=int(s[l:i])
                    item = s[i+1:(i+length+1)]
                    result.append(item)
                    l=(i+length+1)
                    i=i+length+1
            i+=1
        return result



            
