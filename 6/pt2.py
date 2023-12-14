import re

input = open("./6/input.txt", "r")
times: list[int] = []
distances: list[int] = []

def parse(input) -> tuple[int, int]:
    times: list[int] = []
    distances: list[int] = []
    for line in input:
        if "Time:" in line:
            times = int("".join([x for x in re.split(":", line)[1].strip().split(" ")]))
        if "Distance:" in line:
            distances = int("".join([x for x in re.split(":", line)[1].strip().split(" ")]))
    return (times, distances)

values = parse(input)

def calc_distance(time: int, max_distance: int) -> int:
    return len([(time - i) * i for i in range(1, time) if (time - i) * i > max_distance])

val = calc_distance(values[0], values[1])

print(val)
