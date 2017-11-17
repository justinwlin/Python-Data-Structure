class MatrixPosition():
    def __init__(self, row = 1, col = 1, direction = ""):
        self.row = row
        self.col = col
        self.direction = direction

    def __eq__(self, other):
        return (self.row == other.row and
                self.col == other.col and
                self.direction == other.direction)

    def __repr__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"

temp_file = open("maze.txt")
lines = temp_file.readlines()
temp_file.close


maze = []
for item in lines:
    maze.append(item.split())
# for row in maze:
#     for item in row:
#         print(item, " ", end="")
#     print()

def maze_algorithm(maze):
    player = MatrixPosition()
    possiblePosition = []
    if maze[player.row - 1][player.col] == '0':
        possiblePosition.append("UP")
    if maze[player.row + 1][player.col] == '0':
        possiblePosition.append("DOWN")
    if maze[player.row][player.col - 1] == '0':
        possiblePosition.append("LEFT")
    if maze[player.row][player.col + 1] == '0':
        possiblePosition.append("RIGHT")


maze_algorithm(maze)