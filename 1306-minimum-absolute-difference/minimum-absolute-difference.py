class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = [0]*len(arr)
        result[0] = abs(arr[0])
        for i in range(1, len(arr)):
            result[i] = abs(arr[i]-arr[i-1])
        difference = min(result[1:])
        result = []
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) == difference:
                result.append([arr[i-1], arr[i]])
        return result
