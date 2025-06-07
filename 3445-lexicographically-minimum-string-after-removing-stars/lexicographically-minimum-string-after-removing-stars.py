class Solution:
    def clearStars(self, s: str) -> str:
        if "*" not in s:
            return s
        heap = []
        deleted = set()
        for i, char in enumerate(s):
            if char == '*':
                char, neg = heapq.heappop(heap)
                deleted.add(-neg)
            else:
                heapq.heappush(heap, (char, -i))
        res = []
        for i, c in enumerate(s):
            if i in deleted or c=='*':
                continue
            res.append(c)
        return ''.join(res)