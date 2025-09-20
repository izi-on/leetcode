from collections import defaultdict


class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = defaultdict(lambda: [0 for _ in range(rows + 1)])

    def _get_cell_coordinates(self, cell: str):
        return (cell[0], int(cell[1:]))

    def _extract_value_of_cell(self, cell):
        col, row = self._get_cell_coordinates(cell)
        return self.grid[col][row]

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._get_cell_coordinates(cell)
        self.grid[col][row] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def _parse_formula(self, formula) -> tuple[str, str]:
        return formula[1:].split("+")

    def _is_number(self, to_add: str):
        if all([c.isdigit() for c in to_add]):
            return True
        return False

    def getValue(self, formula: str) -> int:
        left, right = self._parse_formula(formula)
        result = 0
        for to_add in [left, right]:
            if self._is_number(to_add):
                result += int(to_add)
            else:  # is cell
                result += self._extract_value_of_cell(to_add)
        return result


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
