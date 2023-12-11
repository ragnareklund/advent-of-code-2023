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
        return len(self.winnings.intersection(self.numbers))
    
    def cards(self) -> list[int]:
        points = self.points()
        # print(f"Copies: {points}")
        return [n + self.id for n in range(1, points + 1)]

games: dict[int, Game] = dict()
game_copies: dict[int, list[Game]] = dict()

for line in input:
    id_str, winnings_str, numbers_str = re.split(r":|\|", line)
    id = int(re.split(r" +", id_str)[1])
    winnings = set([int(n) for n in winnings_str.strip().split(" ") if n != ""])
    numbers = set([int(n) for n in numbers_str.strip().split(" ") if n != ""])
    game: Game = Game(id, winnings, numbers)
    games[id] = game
    game_copies[id] = [game]

def copy_games(ids: list[int]) -> None:
    for id in ids:
        game_copies[id].append(games[id])

for id in game_copies:
    for game in game_copies[id]:
        copy_games(game.cards())

cards = [len(games) for games in game_copies.values()]
print(sum(cards))