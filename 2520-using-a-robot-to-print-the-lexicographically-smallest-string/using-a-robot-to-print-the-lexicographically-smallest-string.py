class Solution:
    def robotWithString(self, s: str) -> str:
        min_char = min(s)
        min_char_count = s.count(min_char)

        res, t, last_idx = "", [], len(s)-1

        for idx, char in enumerate(s):
            if char == min_char:
                res += char
                min_char_count -=1
                if min_char_count == 0:
                    if idx>=last_idx:
                        break
                    min_char = min(s[idx+1:])
                    min_char_count = s[idx+1:].count(min_char)
                    while t and t[-1] <= min_char:
                        res+=t.pop()
            else:
                t.append(char)
        return res+"".join(t[::-1])
