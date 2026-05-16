class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""  
        for string in strs:
            n = len(string)
            output += str(n) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        output = [] 
        i = 0 
        while i < len(s): 
            j  = s.find("#", i)
            L = int(s[i:j])

            start = j + 1 
            output.append(s[start: start+L])
            i = start + L 
        return output 
