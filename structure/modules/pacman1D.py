
from getchar import Getch

game = ".............................................................................."
pac_pos = 40

get_char = Getch()
print()

while '.' in game:
    # update and print the 1D playing field
    game = game[:pac_pos]+' '+game[pac_pos+1:]
    print('\r'+game[:pac_pos]+'G'+game[pac_pos+1:], end="")
    
    # read a character
    char = get_char()
    if ord(char) in (68,75):
        # handle move to the left
        pac_pos -= 1
        if pac_pos == -1: 
            pac_pos = 77
    elif ord(char) in (67,77):
        # handle move to the right
        pac_pos += 1
        if pac_pos == 78: 
            pac_pos = 0
