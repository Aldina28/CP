class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # result = []
        # for i in range(len(candies)):
        #     if candies[i]+extraCandies >= max(candies):
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        # result = []
        # for candy in candies:
        #     if candy+extraCandies >= max(candies):
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        result = []
        for i in range(len(candies)):
            result.append(candies[i]+extraCandies>=max(candies))
        return result