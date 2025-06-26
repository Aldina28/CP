class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0  # number of characters in the valid subsequence
        value = 0  # current value of the binary subsequence
        power = 1  # current power of 2 (for binary digit weight)

        # Traverse the string from right to left
        for ch in reversed(s):
            if ch == '0':
                count += 1  # Always safe to include 0
            else:
                if power <= k and value + power <= k:
                    value += power
                    count += 1
                # else, skip this '1' as it would exceed k

            power <<= 1  # move to the next bit (multiply power by 2)
            if power > k:  # Further bits would be too big
                break

        # Count all the '0's we skipped before and any '1's we could take
        count += s[:len(s) - count].count('0')

        return count