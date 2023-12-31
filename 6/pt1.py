import re

input = open("./6/input.txt", "r")
times: list[int] = []
distances: list[int] = []

def parse(input) -> list[tuple[int, int]]:
    times: list[int] = []
    distances: list[int] = []
    for line in input:
        if "Time:" in line:
            times = [int(x) for x in re.split(":", line)[1].strip().split(" ") if x != ""]
        if "Distance:" in line:
            distances = [int(x) for x in re.split(":", line)[1].strip().split(" ") if x != ""]
    return list(zip(times, distances))

values = parse(input)

def calc_distance(time: int, max_distance: int) -> int:
    return len([(time - i) * i for i in range(1, time) if (time - i) * i > max_distance])

val: int = 1
for value in values:
    val = val * calc_distance(value[0], value[1])

print(val)
