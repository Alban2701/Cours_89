import random as rd

teams = ["A", "B", "C", "D"]
rd.shuffle(teams)
bets = {"A": 0, "B": 0, "C": 0, "D": 0}
guesses = {"A": "", "B": "", "C": "", "D": ""}
scores = {"A": 0, "B": 0, "C": 0, "D": 0}

def take_guesses():
    for team in teams:
        guesses[team] = input(f"Guess de l'équipe '{team}' -> ")
        bet = input(f"Pari de l'équipe '{team}' -> ")
        while not bet.isdigit():
            bet = input(f"Pari de l'équipe '{team}'") 
        bets[team] = int(bet)

def display_scores():
    for team, score in scores.items():
        print(f"l'équipe {team} a {score} point{"s" if score != 0 else ""}")

def give_points():
    for team, guess in guesses.items():
        print(f"équipe '{team}' a dit '{guess}'")
        won = input("Guess correct: C\nGuess faux: F\nGuess approximatif: A\nEntrée -> ")
        while won.lower() not in ["a", "f", "c"]:
            won = input("Guess correct: C\nGuess faux: F\nGuess approximatif: A")
        match won.lower():
            case "a":
                score = bets[team] / 2
                print(f"l'équipe {team} gagne {score} points")
                scores[team] += score
            case "c":
                score = bets[team]
                print(f"l'équipe {team} gagne {score} points")
                scores[team] += bets[team]
            case "f":
                score = bets[team]
                print(f"l'équipe {team} perd {score} points")
                scores[team] -= bets[team]

in_game = True

while in_game:
    rd.shuffle(teams)
    take_guesses()
    give_points()
    display_scores()
    user_input = input("Continuer ? [o]/n")
    if user_input.lower() == "n":
        in_game = False



