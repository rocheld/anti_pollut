class GameBoard:

    def __init__(self):
        self.row = 0
        self.col = 0
        self.time = 0
        self.board = [[Square(0) for i in range(self.col)] for j in range(self.row)]
        self.cleaner_pos = []

    def load_board(self, filename):
        row_pos = 0
        read_header = False

        with open(filename) as infile:
            for line in infile:
                next_line = line.split(None)

                if read_header is False:
                    self.row = int(next_line[0])
                    self.col = int(next_line[1])
                    self.time = int(next_line[2])
                    self.board = [[Square(0) for i in range(self.col)] for j in range(self.row)]
                    read_header = True

                    print(self.row, self.col, self.time)
                else:

                    for col_pos in range(len(next_line)):

                        # Read next int from file
                        value = int(next_line[col_pos])

                        if value == -1:
                            position = [int(row_pos), int (col_pos)]
                            self.cleaner_pos.append(position)

                        # Load square object and set the value
                        element = self.board[row_pos][col_pos]
                        element.value = value
                        element.pos = [row_pos, col_pos]

                        # Check Left Buddy
                        if row_pos - 1 >= 0:
                            left = [row_pos-1, col_pos]

                            if left not in self.cleaner_pos:
                                element.add_neighbor(left)

                        # Check Right Buddy
                        if row_pos + 1 <= self.row - 1:
                            right = [row_pos+1, col_pos]

                            if right not in self.cleaner_pos:
                                element.add_neighbor(right)

                        # Check upper Buddy
                        if col_pos - 1 >= 0:
                            upper = [row_pos,col_pos-1]

                            if upper not in self.cleaner_pos:
                                element.add_neighbor(upper)

                        # Check lower Buddy
                        if col_pos + 1 <= self.col-1:
                            lower = [row_pos, col_pos+1]

                            if lower not in self.cleaner_pos:
                                element.add_neighbor(lower)

                    row_pos += 1

    def air_flow(self):

        for i in range(len(self.cleaner_pos)):

            curr_loc = [self.cleaner_pos[i][0], self.cleaner_pos[i][1]]
            upper_flow = True

            # set up starting point

            if i is 0:
                if self.has_upper(curr_loc):
                    curr_row = curr_loc[0]
                    curr_col = curr_loc[1]
                    curr_loc = [curr_row - 1, curr_col]

            else:
                upper_flow = False
                if self.has_lower(curr_loc):
                    curr_row = curr_loc[0]
                    curr_col = curr_loc[1]
                    curr_loc = [curr_row + 1, curr_col]

            if upper_flow is True:
                while self.has_upper(curr_loc):

                    curr_row = curr_loc[0]
                    curr_col = curr_loc[1]
                    next_loc = [curr_row - 1, curr_col]

                    curr_square = self.board[curr_loc[0]][curr_loc[1]]
                    next_square = self.board[next_loc[0]][next_loc[1]]

                    curr_square.value = next_square.value
                    curr_loc = next_loc

            else:
                while self.has_lower(curr_loc):

                    curr_row = curr_loc[0]
                    curr_col = curr_loc[1]

                    next_loc = [curr_row + 1, curr_col]

                    curr_square = self.board[curr_loc[0]][curr_loc[1]]
                    next_square = self.board[next_loc[0]][next_loc[1]]

                    curr_square.value = next_square.value
                    curr_loc = next_loc

            while self.has_right(curr_loc):

                curr_row = curr_loc[0]
                curr_col = curr_loc[1]

                next_loc = [curr_row, curr_col + 1]
                curr_square = self.board[curr_loc[0]][curr_loc[1]]
                next_square = self.board[next_loc[0]][next_loc[1]]

                curr_square.value = next_square.value
                curr_loc = next_loc

            if upper_flow is True:
                while self.has_lower(curr_loc) and curr_loc[0] != self.cleaner_pos[0][0]:

                    curr_row = curr_loc[0]
                    curr_col = curr_loc[1]

                    next_loc = [curr_row + 1, curr_col]
                    curr_square = self.board[curr_loc[0]][curr_loc[1]]
                    next_square = self.board[next_loc[0]][next_loc[1]]

                    curr_square.value = next_square.value
                    curr_loc = next_loc
            else:
                while self.has_upper(curr_loc) and curr_loc[0] != self.cleaner_pos[1][0]:

                    curr_row = curr_loc[0]
                    curr_col = curr_loc[1]

                    next_loc = [curr_row - 1, curr_col]
                    curr_square = self.board[curr_loc[0]][curr_loc[1]]
                    next_square = self.board[next_loc[0]][next_loc[1]]

                    curr_square.value = next_square.value
                    curr_loc = next_loc

            while self.has_left(curr_loc):

                curr_row = curr_loc[0]
                curr_col = curr_loc[1]

                next_loc = [curr_row, curr_col - 1]

                curr_square = self.board[curr_loc[0]][curr_loc[1]]
                next_square = self.board[next_loc[0]][next_loc[1]]

                if next_square.is_not_cleaner():
                    curr_square.value = next_square.value

                else:
                    curr_square.value = 0

                curr_loc = next_loc

    def has_upper(self, loc):
        result = False
        curr_row = loc[0]

        if curr_row - 1 >= 0:
            result = True

        return result

    def has_lower(self, loc):

        result = False
        curr_row = loc[0]

        if curr_row + 1 <= self.row -1:
            result = True
        return result

    def has_left(self, loc):

        result = False
        curr_col = loc[1]

        if curr_col -1 >= 0:
            result = True

        return result

    def has_right(self, loc):

        result = False
        curr_row = loc[0]
        curr_col = loc[1]

        if curr_col + 1 <= self.col - 1:
            result = True

        return result

    def spread(self):

        for row_pos in range(self.row):
            for col_pos in range(self.col):

                # access square element
                element = self.board[row_pos][col_pos]

                if element.is_not_cleaner():
                    neighbors = element.neighbors
                    neighbor_counts = element.neighbor_counts()

                    # get the pollution from the neighbor
                    influence = int (element.value / 5)
                    element.value = int(element.value - influence * neighbor_counts)

                    for i in range(neighbor_counts):

                        # Get neighbor's coordinates
                        neighbor_pos = neighbors[i]
                        row_pos = neighbor_pos[0]
                        col_pos = neighbor_pos[1]

                        # Access neighbor
                        neighbor = self.board[row_pos][col_pos]
                        neighbor.set_influence(influence)

        for row_pos in range(self.row):
            for col_pos in range(self.col):
                element = self.board[row_pos][col_pos]

                if element.is_not_cleaner():
                    element.value = element.value + element.influence
                    element.influence = 0

    def get_sum(self):

        sum = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j].is_not_cleaner():
                    sum += self.board[i][j].value

        print("Total: ", sum)

    def print_board(self):
        for i in range(self.row):
            print("")
            for j in range(self.col):
                element = self.board[i][j]
                print(element.value, " ", end='')

        print("")


class Square(object):

    def __init__(self, value):
        self.value = value
        self.influence = 0
        self.pos = []
        self.neighbors = []

    def add_neighbor(self, buddy):
        self.neighbors.append(buddy)

    def set_influence(self, influence):
        self.influence += influence

    def is_not_cleaner(self):
        return self.value != -1

    def neighbor_counts(self):
        return len(self.neighbors)
