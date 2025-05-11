class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for l in range(len(arr)-2):
            if arr[l]%2!=0:
                if arr[l+1]%2!=0 and arr[l+2]%2!=0:
                    return True
        return False