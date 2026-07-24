
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rleCodes = {}

        for astr in strs:
            code = self.rle_code(astr)

            if code not in rleCodes:
                rleCodes[code] = []

            rleCodes[code].append(astr)

        return list(rleCodes.values())

    def rle_code(self, s: str):
        m = {}

        for ch in s:
            m[ch] = m.get(ch, 0) + 1

        code = ""

        for ch in sorted(m):
            code += f"{ch}{m[ch]}"

        return code