import time

def start_the_game():
    print("THE LOST KINGDOM")

    time.sleep(2)
    print('Hello Prince!')
    time.sleep(3)
    print('Welcome to The Lost Kingdom')
    print()
    time.sleep(2)

    game_start = input('Would you like to start the game? yes(y) or no(n) (Y/N): ')
    print()
    time.sleep(1)
    if game_start == 'n' or game_start == 'N':
        print('Sad to see you go :( ')
        quit()
    elif game_start == 'Y' or game_start == 'y':
        game_begin()

    else:
        print("Error|| wrong input")
        print()
        time.sleep(2)
        print('type "y" for yes or "n" for no')
        print()
        start_game()


def game_begin():
    import gameintro
    gameIntro.gameintro_start()


print()
print()
start_the_game()


