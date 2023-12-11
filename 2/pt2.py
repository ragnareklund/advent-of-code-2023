import re

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
    min_red = 0
    min_green = 0
    min_blue = 0

    def __init__(self, input: str) -> None:
        self._parse(input)

    def _parse(self, input: str) -> None:
        parsed_game = re.search(r"Game (\d+):(.*)", input)
        self.id = int(parsed_game.group(1))
        self.rounds = [Round(x) for x in parsed_game.group(2).split(";")]
        for round in self.rounds:
            self._min_colors(round)

    def _min_colors(self, round: Round) -> None:
        self.min_red = max(self.min_red, round.red)
        self.min_green = max(self.min_green, round.green)
        self.min_blue = max(self.min_blue, round.blue)

    def pow(self) -> int:
        return self.min_red * self.min_green * self.min_blue

input = open("./2/input.txt", "r")
games = [Game(x) for x in input]
input.close()

game_pows = [game.pow() for game in games]

game_pow_sum = sum(game_pows)

print(game_pow_sum)
