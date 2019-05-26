from board import Board
string = input('Hello! Do you want to play a Tic Tac Toe?\nEnter yes or no\n')
if string == 'yes':
    game = Board()
    while True:
        s = game.choose_the_position()
        game.board = s

        if Board.check_the_status(game.board) is not None:
            if Board.check_the_status(game.board) == 'O':
                print('YOU WON! CONGRATULATIONS!!!')
            else:
                print('YOU ARE LOOSER, HAHA! THE COMPUTER WON!')
            break
        print(game)

        if game.free_position():
            while True:
                position_1 = input('Enter the X position: 1, 2 or 3\n')
                position_2 = input('Enter the Y position: 1, 2 or 3\n')
                position_1 = int(position_1)
                position_2 = int(position_2)
                position_1 -= 1
                position_2 -= 2
                try:
                    game.put_symbol([position_1, position_2], Board.user_symbol)
                    break
                except ValueError:
                    print('You enter the bad position or the board is already filled')

                if Board.check_the_status(game.board) is not None:
                    if Board.check_the_status(game.board) == 'O':
                        print('YOU WON! CONGRATULATIONS!!!')
                    else:
                        print('YOU ARE LOOSER, HAHA! THE COMPUTER WON!')
                    break
        else:
            print('NOBODY WINS((((((')

else:
    print(':((((')
