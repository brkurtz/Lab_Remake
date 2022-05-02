import random

def game():
    # Rock = 1 Paper = 2 Scissor = 3
    score = 0
    player = 0
    comp = 0
    comp_action = ''
    for i in range(3):
        # give computer action
        comp = random.randint(1, 3)
        if comp == 1:
            comp_action = 'rock'
        elif comp == 2:
            comp_action = 'paper'
        else:
            comp_action = 'scissor'
        # assign player with number to check against
        player_action = input('Enter response:').strip().lower()
        while True:
            if player_action == 'rock' or player_action == 'paper' or player_action == 'scissor':
                break
            else:
                player_action = input("Enter valid response:").strip().lower()

        if player_action == 'rock':
            player = 1
        elif player_action == 'paper':
            player = 2
        elif player_action == 'scissor':
            player = 3
        # decide outcome
        if comp == player:
            outcome = 'tie'
        elif (comp == 1 and player == 3) or (comp == 2 and player == 1) or (comp == 3 and player == 2):
            outcome = 'lose'
            score -= 1
        else:
            outcome = 'win'
            score += 1
        # return results
        print(f'Computer is {comp_action}. You are {player_action}. You {outcome}')
        # score breakout if 2 wins or 2 loses
        if score == 2 or score == -2:
            break
    if score == 0:
        print("GAME OVER - IT'S A TIE")
    elif score < 0:
        print('GAME OVER - COMPUTER WINS')
    elif score > 0:
        print("GAME OVER - YOU WIN")


def main():
    print('----------------------')
    print('Rock - Paper - Scissor')
    print('----------------------')
    game()


if __name__ == '__main__':
    main()