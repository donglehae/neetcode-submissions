class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = '\n'.join(strs)
        return encoded_string + f"\n{len(strs)}"
    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split('\n')
        return decoded_strs[:-1] if int(decoded_strs[-1]) > 0 else []