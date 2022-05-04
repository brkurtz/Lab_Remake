from RPSgui import *

def main():

    """
    Window controls
    """
    window = Tk()
    window.title('Rock, Paper, Scissors')
    window.geometry('400x200')
    window.resizable(False, False)
    widgets = RPSgui(window)
    window.mainloop()


if __name__ == '__main__':
    main()



