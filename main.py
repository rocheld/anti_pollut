

if __name__ == "__main__":

    # check the  style guide for import!
    from Board import GameBoard

    filename = "file1.txt"

    print("running")
    board = GameBoard()
    board.load_board(filename)

    game_time = board.time
    time = 0
    board.print_board()

    while time < game_time:

        time += 1
        board.spread()
        board.air_flow()

    board.print_board()
    board.get_sum()
