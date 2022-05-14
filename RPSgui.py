from tkinter import *
import random
import time

outcomes = {
    'rock': {'rock': 1, 'paper': 0, 'scissors': 2},
    'paper': {'rock': 2, 'paper': 1, 'scissors': 0},
    'scissors': {'rock': 0, 'paper': 2, 'scissors': 1}
}

player_score = 0
comp_score = 0
round_counter = 1
max_round = 0
computer_choice = ''
player_choice = ''


class RPSgui:
    """
    This defines the box for playing the game in
    """

    def __init__(self, window) -> None:
        """
        This initializes the welcome screen for the
        :param window: window name for tkinter
        """
        # Empty widgets for after the game starts
        self.label_outcome = None
        self.frame_outcome = None
        self.choice_scissors = None
        self.choice_paper = None
        self.choice_rock = None
        self.frame_choices = None
        self.label_scores_comp = None
        self.label_counter = None
        self.frame_scores = None
        self.frame_counter = None
        self.label_scores_player = None

        # Start
        self.window = window

        # Title
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Rock Paper Scissors', font=('BOLD', 18))
        self.frame_name.pack(side='top', anchor='center')
        self.label_name.pack(side='top', anchor='center')

        # Welcome message
        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text="Welcome please select a number of rounds to play:",
                                   font=16)
        self.frame_message.pack(side='top', anchor='center', pady=10)
        self.label_message.pack(anchor='center')

        # Round options
        self.frame_rounds = Frame(self.window)
        self.label_rounds = Label(self.frame_rounds, text="Rounds:", font=14)
        self.radio_round = IntVar()
        self.radio_round.set(0)
        self.radio_3 = Radiobutton(self.frame_rounds, text='3', variable=self.radio_round, value=1, font=14)
        self.radio_5 = Radiobutton(self.frame_rounds, text='5', variable=self.radio_round, value=2, font=14)
        self.radio_7 = Radiobutton(self.frame_rounds, text='7', variable=self.radio_round, value=3, font=14)
        self.frame_rounds.pack(anchor='center')
        self.label_rounds.pack(padx=4, side='left')
        self.radio_3.pack(side='left')
        self.radio_5.pack(side='left')
        self.radio_7.pack(side='left')

        self.button_go = Button(self.window, text='Go!', command=self.start)
        self.button_go.pack(anchor='center')

        self.count_hold = StringVar()
        self.player_score_hold = StringVar()
        self.comp_score_hold = StringVar()

    def start(self) -> None:
        """
        This method starts the game if a radio option is selected
        :return:
        """
        global player_score
        global comp_score
        global max_round
        status = self.radio_round.get()
        if status > 0:
            for widget in self.window.winfo_children():
                widget.destroy()

            if status == 1:
                max_round = 3

            if status == 2:
                max_round = 5
            if status == 3:
                max_round = 7

        # Title
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Rock Paper Scissors', font=('BOLD', 18))
        self.frame_name.pack(side='top', anchor='center')
        self.label_name.pack(side='top', anchor='center')

        # Round counter
        self.frame_counter = Frame(self.window)
        self.label_counter = Label(self.frame_counter, text=f'Round Count: {round_counter}', font=('BOLD', 18))
        self.frame_counter.pack(anchor='center')
        self.label_counter.pack(anchor='center')

        # Scores
        self.frame_scores = Frame(self.window)
        self.label_scores_player = Label(self.frame_scores, text=f'Player Score: {player_score}')
        self.label_scores_comp = Label(self.frame_scores, text=f'Computer Score: {comp_score}')
        self.frame_scores.pack()
        self.label_scores_player.pack(side='left', anchor='w')
        self.label_scores_comp.pack(side='right', anchor='e')

        # Choice buttons
        self.frame_choices = Frame(self.window)
        self.choice_rock = Button(self.frame_choices, text='rock', command=self.rock)
        self.choice_paper = Button(self.frame_choices, text='paper', command=self.paper)
        self.choice_scissors = Button(self.frame_choices, text='scissors', command=self.scissors)
        self.frame_choices.pack(anchor='center')
        self.choice_rock.pack(side='left', padx=20)
        self.choice_paper.pack(side='left', padx=20)
        self.choice_scissors.pack(side='left', padx=20)

        # Outcome Message
        self.frame_outcome = Frame(self.window)
        self.label_outcome = Label(self.frame_outcome, fg='blue')
        self.frame_outcome.pack(anchor='center')
        self.label_outcome.pack()

    def rock(self) -> None:
        """
        This method calculates the round for the computer and updates the score based on the player choosing rock.
        :return:
        """
        global player_score
        global comp_score
        global round_counter
        global computer_choice
        global player_choice
        options = ['rock', 'paper', 'scissors']
        rand = random.randint(0, 2)
        computer_choice = options[rand]
        player_choice = 'rock'
        result = outcomes[player_choice][computer_choice]
        if round_counter <= max_round:
            round_counter = round_counter + 1
            if result == 2:
                player_score = player_score + 2
            elif result == 1:
                player_score = player_score + 1
                comp_score = comp_score + 1
            elif result == 0:
                comp_score = comp_score + 2
        self.update()

    def paper(self) -> None:
        """
        This method calculates the round for the computer and updates the score based on the player choosing paper.
        :return:
        """
        global player_score
        global comp_score
        global round_counter
        global computer_choice
        global player_choice
        options = ['rock', 'paper', 'scissors']
        rand = random.randint(0, 2)
        computer_choice = options[rand]
        player_choice = 'paper'
        result = outcomes[player_choice][computer_choice]
        if round_counter <= max_round:
            round_counter = round_counter + 1
            if result == 2:
                player_score = player_score + 2
            elif result == 1:
                player_score = player_score + 1
                comp_score = comp_score + 1
            elif result == 0:
                comp_score = comp_score + 2
        self.update()

    def scissors(self) -> None:
        """
        This method calculates the round for the computer and updates the score based on the player choosing scissors
        :return:
        """
        global player_score
        global comp_score
        global round_counter
        global computer_choice
        global player_choice
        options = ['rock', 'paper', 'scissors']
        rand = random.randint(0, 2)
        computer_choice = options[rand]
        player_choice = 'scissors'
        result = outcomes[player_choice][computer_choice]
        if round_counter <= max_round:
            round_counter = round_counter + 1
            if result == 2:
                player_score = player_score + 2
            elif result == 1:
                player_score = player_score + 1
                comp_score = comp_score + 1
            elif result == 0:
                comp_score = comp_score + 2
        self.update()

    def update(self):
        """
        This method updates the screen after a button is pressed
        :return:
        """
        self.label_outcome.config(text=f'You chose {player_choice} and the computer chose {computer_choice}')
        self.label_scores_player.config(text='Player Score:' + str(player_score))
        self.label_scores_comp.config(text='Computer Score:' + str(comp_score))

        if round_counter <= max_round:
            self.label_counter.config(text='Round Counter:' + str(round_counter))
        else:
            self.choice_rock.config(state='disabled')
            self.choice_paper.config(state='disabled')
            self.choice_scissors.config(state='disabled')
            if player_score > comp_score:
                self.label_outcome.config(text=f'You chose {player_choice} and the computer chose {computer_choice}\n '
                                               'You beat the computer!')
            elif player_score == comp_score:
                self.label_outcome.config(text=f'You chose {player_choice} and the computer chose {computer_choice}\n '
                                               'You tied with the computer')
            else:
                self.label_outcome.config(text=f'You chose {player_choice} and the computer chose {computer_choice}'
                                               '\nYou lost to the computer')

