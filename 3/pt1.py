import re

GRID = []

class Coordinate:
    """A position in the scheme"""
    x: int = None
    y: int = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

class Number:
    """A number on the scheme"""
    len: int = None
    val: int = None

    def __init__(self, val: str) -> None:
        self.len = len(val)
        self.val = int(val)

class Symbol:
    """A symbol"""
    val: str = None
    len: int = 1

    def __init__(self, val: str) -> None:
        self.val = val

symbols: [Coordinate] = []

def parse_val(val: str) -> None | Number | Symbol:
    if re.match(r"\.+", val):
        return None
    elif re.match(r"\d+", val):
        return Number(val)
    else:
        return Symbol(val)

def parse_input(line: str, y: int) -> None:
    res = [str(z) for z in re.findall(r"(\.+|\d+|.)", line) if z not in ["", "\n"]]
    x: int = 0
    for val in res:
        obj = parse_val(val)
        for char in val:
            if isinstance(obj, Symbol):
                symbols.append(Coordinate(len(GRID[y]), y))
            GRID[y].append(obj)

def check_surrounding_numbers(c: Coordinate) -> set[Number]:
    numbers: set[Number] = set()
    surrondings = [{"x": -1, "y": -1},
    {"x": 0, "y": -1},
    {"x": 1, "y": -1},
    {"x": -1, "y": 0},
    {"x": 1, "y": 0},
    {"x": -1, "y": 1},
    {"x": 0, "y": 1},
    {"x": 1, "y": 1}]
    for pos in surrondings:
        x = c.x + pos["x"]
        y = c.y + pos["y"]
        if  0 > x > 140 or 0 > y > 140:
            continue
        val = GRID[y][x]
        if isinstance(val, Number):
            numbers.add(val)
    return numbers

input = open("./3/input.txt", "r")
y = 0
for line in input:
    GRID.append([])
    parse_input(line, y)
    y = y+1
input.close()

surrounding_numbers = [check_surrounding_numbers(x) for x in symbols]
vals: set[Number] = set()
for numbers in surrounding_numbers:
    for number in numbers:
        vals.add(number)
nums = [val.val for val in vals]
print(sum(nums))