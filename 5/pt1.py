import re

input = open("./5/input.txt", "r")

class Range:
    """A range of some kind"""

    start: int = 0
    stop: int = 0

    def __init__(self, start: int, length: int) -> None:
        self.start = start
        self.stop = start + length

    def in_range(self, val: int) -> bool:
        return self.start <= val < self.stop
    
    def pos(self, val: int) -> int:
        return val - self.start
    
    def __str__(self) -> str:
        return f"Range[start: {self.start}, stop: {self.stop}]"

class Mapper:
    """Maps from one to another"""

    name: str = "mapper"
    from_ranges: list[Range] = None
    to_ranges: list[Range] = None

    def __init__(self, name: str) -> None:
        self.name = name
        self.from_ranges = []
        self.to_ranges = []

    def add_range(self, from_range: Range, to_range: Range):
        self.from_ranges.append(from_range)
        self.to_ranges.append(to_range)

    def map(self, val: int) -> int:
        for i, range in enumerate(self.from_ranges):
            if range.in_range(val):
                mapped_value = self.to_ranges[i].start + range.pos(val)
                print(f"value {val} found in range: {range}: mapped value: {mapped_value}")
                return mapped_value
        return val

seeds: list[int] = []
mappers: list[Mapper] = []

def parse():
    for line in input:
        if re.match(r"seeds:", line):
            for val in re.split(r" +", line.split(":")[1].strip()):
                seeds.append(int(val))
        elif "map:" in line:
            mappers.append(Mapper(line))
        elif re.match(r"\d+ +\d+ +\d+", line):
            to, fr, le = [int(x) for x in re.split(r" +", line)]
            mappers[-1].add_range(Range(fr, le), Range(to, le))

def map(val: int) -> int:
    last_val = val
    print(f"seed: {last_val}")
    for m in mappers:
        last_val = m.map(last_val)
    return last_val

parse()
vals = [map(seed) for seed in seeds]
print(vals)
print(min(vals))