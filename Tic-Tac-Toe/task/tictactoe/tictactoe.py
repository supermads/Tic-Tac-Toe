# write your code here

def print_grid(coord_grid):
    print("---------")
    print("| {} {} {} |".format(coord_grid[0][2], coord_grid[1][2], coord_grid[2][2]))
    print("| {} {} {} |".format(coord_grid[0][1], coord_grid[1][1], coord_grid[2][1]))
    print("| {} {} {} |".format(coord_grid[0][0], coord_grid[1][0], coord_grid[2][0]))
    print("---------")


def make_move(coord_grid):
    a, b = input("Enter the coordinates: ").split()
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("You should enter numbers!")
        return
    if a < 1 or a > 3 or b < 1 or b > 3:
        print("Coordinates should be from 1 to 3!")
        return 
    elif coord_grid[a - 1][b - 1]:
        print("This cell is occupied! Choose another one!")
        return 
    else:
        return a - 1, b - 1


def find_winner(grid):
    winner = ''
    acc = 0
    rows = [[grid[0], grid[1], grid[2]], [grid[3], grid[4], grid[5]], [grid[6], grid[7], grid[8]]]
    columns = [[grid[0], grid[3], grid[6]], [grid[1], grid[4], grid[7]], [grid[2], grid[5], grid[8]]]
    diagonals = [[grid[0], grid[4], grid[8]], [grid[1], grid[4], grid[7]], [grid[2], grid[4], grid[6]]]
    for row in rows:
        if row[0] == row[1] == row[2]:
            winner = row[0]
            acc += 1
    for column in columns:
        if column[0] == column[1] == column[2]:
            winner = column[0]
            acc += 1
    for diagonal in diagonals:
        if diagonal[0] == diagonal[1] == diagonal[2]:
            winner = diagonal[0]
            acc += 1
    if acc <= 1:
        return winner
    else:
        return "impossible"


def main():
    grid = list(input("Enter cells: "))
    coord_grid = [[grid[6], grid[3], grid[0]], [grid[7], grid[4], grid[1]], [grid[8], grid[5], grid[2]]]
    print_grid(coord_grid)
    keep_playing = True
    while keep_playing:
        a, b = input("Enter the coordinates: ").split()
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print("You should enter numbers!")
        if a < 1 or a > 3 or b < 1 or b > 3:
            print("Coordinates should be from 1 to 3!")
        elif coord_grid[a - 1][b - 1] == 'X' or coord_grid[a - 1][b - 1] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            coord_grid[a - 1][b - 1] = "X"
            print_grid(coord_grid)
            keep_playing = False
  
        

main()
