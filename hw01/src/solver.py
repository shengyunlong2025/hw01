from typing import List

class EightQueensSolver:
    def __init__(self, n: int = 8):
        self.n = n
        self.solutions: List[List[int]] = []

    def solve(self) -> List[List[int]]:
        self.solutions.clear()
        self._backtrack(0, [])
        return self.solutions

    def _backtrack(self, row: int, current: List[int]):
        if row == self.n:
            self.solutions.append(current[:])
            return
        for col in range(self.n):
            if self._is_safe(row, col, current):
                current.append(col)
                self._backtrack(row + 1, current)
                current.pop()

    def _is_safe(self, row: int, col: int, current: List[int]) -> bool:
        # 故意 Bug
        for r, c in enumerate(current):
            if c == col or abs(c + col) == row - r:  # <- 错误的对角线判断
                return False
        return True

    @staticmethod
    def format_board(solution: List[int]) -> List[str]:
        n = len(solution)
        board = []
        for col in solution:
            row_str = ['.'] * n
            row_str[col] = 'Q'
            board.append(''.join(row_str))
        return board

if __name__ == "__main__":
    solver = EightQueensSolver()
    sols = solver.solve()
    print(f"Total solutions: {len(sols)}")

