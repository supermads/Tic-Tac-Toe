# write your code here

def print_grid(grid):
    print("---------")
    print("| {} {} {} |".format(grid[0], grid[1], grid[2]))
    print("| {} {} {} |".format(grid[3], grid[4], grid[5]))
    print("| {} {} {} |".format(grid[6], grid[7], grid[8]))
    print("---------")


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
    print_grid(grid)
    x_count = grid.count("X")
    o_count = grid.count("O")
    winner = find_winner(grid)
    if x_count >= (o_count + 2) or o_count >= (x_count + 2) or winner == "impossible":
        print("Impossible")
    elif not winner:
        if x_count + o_count == 9:
            print("Draw")
        else:
            print("Game not finished")
    else:
        print("{} wins".format(winner))
        

main()
