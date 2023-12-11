import re

input = open("./5/input.txt", "r")

class Range:
    """A range of some kind"""

    start: int = 0
    stop: int = 0

    def __init__(self, start: int, stop: int) -> None:
        if stop < start:
            raise Exception(f"Start {start:,} större än stopp {stop:,}")
        else:
            self.start = start
            self.stop = stop

    def in_range(self, val: int) -> bool:
        return self.start <= val < self.stop
    
    def pos(self, val: int) -> int:
        return val - self.start
    
    def __lt__(self, other) -> int:
        return self.start - other.start
    
    def __str__(self) -> str:
        return f"Range[start: {self.start:,} stop: {self.stop:,}]"
    
    def __repr__(self) -> str:
        return self.__str__()

class Mapper:
    """Maps from one to another"""

    name: str = "mapper"
    range_maps: list[tuple[Range, Range]]

    def __init__(self, name: str) -> None:
        self.name = name
        self.range_maps = []

    def __repr__(self) -> str:
        return f"{self.name} maps: {self.range_maps}"
    
    def from_ranges(self) -> list[Range]:
        return [r[0] for r in self.range_maps]

    def add_range(self, from_range: Range, to_range: Range):
        self.range_maps.append((from_range, to_range))
        self.range_maps = sorted(self.range_maps, key=lambda r: r[0].start)

    def map(self, val: int) -> int:
        for fr, to in self.range_maps:
            if fr.in_range(val):
                mapped_value = to.start + fr.pos(val)
                # print(f"value {val:,} found in range: {fr}: mapped value: {mapped_value:,} from: {to}")
                return mapped_value
        return val
    
    def map_range(self, input_range: Range, iteration: int = 0) -> list[Range]:
        for from_range, _ in self.range_maps:
            if from_range.stop <= input_range.start:
                # current range is less than input, continue
                continue
            if input_range.start < from_range.start and from_range.in_range(input_range.stop):
                # input starts outside and end inside current range, split it and return
                first_part = Range(input_range.start, from_range.start)
                second_part = Range(from_range.start, input_range.stop)
                return [first_part, second_part]
            if input_range.start < from_range.start and input_range.stop >= from_range.stop:
                # current range is inside input, split and do a recursive split
                first_part = Range(input_range.start, from_range.start)
                second_part = from_range
                rest = self.map_range(Range(from_range.stop, input_range.stop), iteration +1)
                return [first_part, second_part] + rest
            if from_range.in_range(input_range.start) and from_range.stop <= input_range.stop:
                # input range starts in current range and ends outside, recursive split
                first_part = Range(input_range.start, from_range.stop)
                rest = self.map_range(Range(from_range.stop, input_range.stop), iteration +1)
                return [first_part] + rest
            
            # input inside current range, return current range OR
            # input is less than current range, no need to scan more
            return [input_range]
        # input start is greater than all ranges
        return [input_range]

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
            mappers[-1].add_range(Range(fr, fr + le), Range(to, to + le))

def map_range_values(mapper: Mapper, range: Range) -> Range:
    if range.start < range.stop:
        return Range(mapper.map(range.start), mapper.map(range.stop -1) +1)
    elif range.start == range.stop:
        return Range(mapper.map(range.start), mapper.map(range.stop) +1)
    else:
        raise Exception(f"Ogiltig range: {range}")

def map(range: Range) -> list[int]:
    ranges_to_map = [range]
    for m in mappers:
        current_ranges: list[Range] = []
        # print(m.name)
        for r in ranges_to_map:
            current_ranges += m.map_range(r) 
        ranges_to_map = [map_range_values(m, r) for r in current_ranges]
    return [r.stop -1 for r in ranges_to_map] + [r.start for r in ranges_to_map]

def to_seeds(s: list[int]) -> list[Range]:
    ret: list[Range] = []
    for i, seed in enumerate(s):
        if i % 2 == 1:
            continue
        ret.append(Range(s[i], s[i] + s[i+1]))
    return ret

parse()
val: int = None
for seed_range in to_seeds(seeds):
    print(f"seed range: {seed_range}")
    seed_val = min(map(seed_range))
    if val is None or seed_val < val:
        val = seed_val
print(f"VAL:: {val}")