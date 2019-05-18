class GameBoard:

    def __init__(self):
        self.row = 0
        self.col = 0
        self.time = 0
        self.board = [[0 for i in range(self.row)] for j in range(self.col)]
        self.position = []

    def load_board(self,filename):
        row_count = 0
        read_header = False

        with open(filename) as infile:
            for line in infile:
                next_line = line.split(None)

                if read_header is False:
                    self.row = int(next_line[0])
                    self.col = int(next_line[1])
                    self.time = int(next_line[2])
                    self.board = [[0 for i in range(self.row)] for j in range(self.col)]

                    read_header = True

                else:
                    self.board[row_count] = next_line
                    for i in range(len(next_line)):
                        if next_line[i] == "-1":
                            position = [row_count, i]
                            self.position.append(position)
                            print(self.position)

                    row_count += 1

    def print_board(self):
        for i in range(self.row):
            print("")
            for j in range(self.col):
                print(self.board[i][j], end='')






