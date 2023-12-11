import re

input = open("./3/input.txt", "r")

GRID = []

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

class Coordinate:
    """A position in the scheme"""
    x: int = None
    y: int = None
    symbol: Symbol = None

    def __init__(self, x: int, y: int, symbol: Symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

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
            if isinstance(obj, Symbol) and obj.val == "*":
                symbols.append(Coordinate(len(GRID[y]), y, obj))
            GRID[y].append(obj)

def get_gear_ratio(c: Coordinate) -> set[Number]:
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
    if len(numbers) == 2:
        gear_values = list(numbers)
        return gear_values[0].val * gear_values[1].val
    return 0

y = 0
for line in input:
    GRID.append([])
    parse_input(line, y)
    y = y+1

gear_reatios = [get_gear_ratio(x) for x in symbols]
print(sum(gear_reatios))