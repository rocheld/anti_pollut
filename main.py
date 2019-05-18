

if __name__ == "__main__":

    # check the  style guide for import!
    from Board import GameBoard

    filename = "file1.txt"

    print("running")
    board = GameBoard()
    board.print_board()

    board.load_board(filename)
    board.print_board()

