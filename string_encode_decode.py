class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each string in strs
            # save the length of the string in lengths array
            # append string to encoded_str
        # pre-append encoded_str with all lengths and a delimiter
        encoded_str = ''.join(strs)
        lengths = []
        for s in strs:
            lengths.append(str(len(s)))

        result = ','.join(lengths) + ':' + encoded_str

        return result

    def decode(self, s: str) -> List[str]:
        if s == ":": return []

        [lengths_str, encoded_str] = s.split(':', 1)
        lengths = lengths_str.split(',')

        decoded_strs = []
        start = 0
        for length in lengths:
            end = start + int(length)
            decoded_strs.append(encoded_str[start:end])
            start = end
        
        return decoded_strs