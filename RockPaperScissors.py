import random

def play():
    user = input("Which do you choose? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'you tied'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "Player Won!!"

    return "Computer Won!!"

def is_win(player, oppnent):
    # return true if play wins
    # r > s, s > p, p > r
    if (player == 'r' and oppnent == 's') or (player == 's' and oppnent == 'p') or (player == 'p' and oppnent == 'r'):
        return True

print(play())