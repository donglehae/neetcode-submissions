class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(str(len(s)) + "#" + s)
        return "".join(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            decoded_strs.append(s[start:end])
            start = end
        return decoded_strs