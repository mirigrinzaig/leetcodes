class Solution(object):
    def totalNQueens(self, n):
        self.count = 0

        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if is_safe(row, col, cols, diagonals, anti_diagonals):
                    cols.add(col)
                    diagonals.add(row - col)
                    anti_diagonals.add(row + col)

                    backtrack(row + 1, diagonals, anti_diagonals, cols)

                    cols.remove(col)
                    diagonals.remove(row - col)
                    anti_diagonals.remove(row + col)

        def is_safe(row, col, cols, diagonals, anti_diagonals):
            return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

        backtrack(0, set(), set(), set())
        return self.count
