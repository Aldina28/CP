class Solution:
    def kthCharacter(self, k: int) -> str:
        # sb = ['a']
        # while len(sb)<k:
        #     size = len(sb)
        #     for i in range(size):
        #         next_char = chr(ord('a')+((ord(sb[i]) - ord('a')+1)%26))
        #         sb.append(next_char)
        # return sb[k-1]
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
        return chr(ord("a") + ans)