import re

max_red   = 12
max_green = 13
max_blue  = 14

input = open("./2/input.txt", "r")

class Round:
    """A round"""

    red = 0;
    green = 0;
    blue = 0;

    def __init__(self, input: str) -> None:
        self._parse(input)

    def _parse(self, input: str) -> None:
        parts = input.strip().split(",")
        for part in parts:
            number, color = part.strip().split(" ")
            match(color):
                case "red": self.red = int(number)
                case "green": self.green = int(number)
                case "blue": self.blue = int(number)

class Game:
    """A game"""

    id = 0
    rounds = []

    def __init__(self, input: str) -> None:
        self._parse(input)

    def _parse(self, input: str) -> None:
        parsed_game = re.search(r"Game (\d+):(.*)", input)
        self.id = int(parsed_game.group(1))
        self.rounds = [Round(x) for x in parsed_game.group(2).split(";")]

def is_valid_round(round: Round) -> bool:
    return round.red <= max_red and round.green <= max_green and round.blue <= max_blue

def is_valid_game(game: Game) -> bool:
    return all( (is_valid_round(r) for r in game.rounds) )

games = [Game(x) for x in input]

valid_games = [game for game in games if is_valid_game(game)]

valid_games_ids = [game.id for game in valid_games]

print(valid_games_ids)

sum_game_ids = sum(valid_games_ids)

print(sum_game_ids)
