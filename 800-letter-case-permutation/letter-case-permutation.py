class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(i, path):
            if i >= len(s):
                res.append(''.join(path))
                return

            if s[i].isalpha():
                # Choose lowercase
                path.append(s[i].lower())
                backtrack(i + 1, path)
                path.pop()  # undo

                # Choose uppercase
                path.append(s[i].upper())
                backtrack(i + 1, path)
                path.pop()  # undo

            else:
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()  # undo

        backtrack(0, [])
        return res