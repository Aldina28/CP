class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [-1]                             # cells[1] = square 1
        ltr = True
        for r in range(n - 1, -1, -1):           # bottom → top
            row = board[r] if ltr else reversed(board[r])
            cells.extend(row)
            ltr = not ltr
        target = len(cells) - 1                  # n²

        # ---------- 2 · BFS ---------- #
        queue = deque([(1, 0)])                  # (square, moves)
        visited = {1}

        while queue:
            s, m = queue.popleft()

            # a) Already there
            if s == target:
                return m

            # b) One plain roll can finish  (safe because we start on s)
            if s >= target - 6:
                return m + 1

            deepest_plain = None
            for r in range(6, 0, -1):            # rolls 6 → 1
                land = s + r
                if land > target:
                    continue

                dest = cells[land]
                if dest != -1:                   # snake / ladder
                    if dest == target:
                        return m + 1
                    if dest not in visited:
                        visited.add(dest)
                        queue.append((dest, m + 1))
                else:                            # plain landing
                    if deepest_plain is None and land not in visited:
                        deepest_plain = land     # remember ONE

            if deepest_plain is not None:
                visited.add(deepest_plain)
                queue.append((deepest_plain, m + 1))

        return -1 