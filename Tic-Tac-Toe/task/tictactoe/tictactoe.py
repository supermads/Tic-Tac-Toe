# write your code here

def print_grid(grid):
    print("---------")
    print("| {} {} {} |".format(grid[0][2], grid[1][2], grid[2][2]))
    print("| {} {} {} |".format(grid[0][1], grid[1][1], grid[2][1]))
    print("| {} {} {} |".format(grid[0][0], grid[1][0], grid[2][0]))
    print("---------")


def find_winner(grid):
    winner = ''
    rows = [[grid[0][2], grid[1][2], grid[2][2]], [grid[0][1], grid[1][1], grid[2][1]], [grid[0][0], grid[1][0], grid[2][0]]]
    columns = [[grid[0][2], grid[0][1], grid[0][0]], [grid[1][2], grid[1][1], grid[1][0]], [grid[2][2], grid[2][1], grid[2][0]]]
    diagonals = [[grid[0][2], grid[1][1], grid[2][0]], [grid[1][2], grid[1][1], grid[1][0]], [grid[2][2], grid[1][1], grid[0][0]]]
    for row in rows:
        if row[0] == row[1] == row[2]:
            winner = row[0]
    for column in columns:
        if column[0] == column[1] == column[2]:
            winner = column[0]
    for diagonal in diagonals:
        if diagonal[0] == diagonal[1] == diagonal[2]:
            winner = diagonal[0]
    return winner


def main():
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_grid(grid)
    count = 0
    while count < 9:
        a, b = input("Enter the coordinates: ").split()
        try:
            a = int(a) - 1
            b = int(b) - 1
        except ValueError:
            print("You should enter numbers!")
        if a < 0 or a > 2 or b < 0 or b > 2:
            print("Coordinates should be from 1 to 3!")
        elif grid[a][b] == 'X' or grid[a][b] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            if count % 2 == 0:
                grid[a][b] = "X"
            else:
                grid[a][b] = "O"
            count += 1
            print_grid(grid)
    winner = find_winner(grid)
    if not winner:
        print("Draw")
    else:
        print("{} wins".format(winner))
        

main()
