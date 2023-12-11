import re

input = open("./4/input.txt", "r")

class Game:
    id: int = None
    winnings: set[int] = []
    numbers: set[int] = []

    def __init__(self, id: int, winnings: set[int], numbers: set[int]) -> None:
        self.id = id
        self.winnings = winnings
        self.numbers = numbers

    def points(self) -> int:
        wins = self.winnings.intersection(self.numbers)
        return int(pow(2, len(wins) -1))
        
games: list[Game] = []

for line in input:
    id_str, winnings_str, numbers_str = re.split(r":|\|", line)
    id = int(re.split(r" +", id_str)[1])
    winnings = set([int(n) for n in winnings_str.strip().split(" ") if n != ""])
    numbers = set([int(n) for n in numbers_str.strip().split(" ") if n != ""])
    games.append(Game(id, winnings, numbers))

print(sum([game.points() for game in games]))
