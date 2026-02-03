def solve_n_Queens(n):
    board = [[". "] * n  for _ in range(n)]

    used_cols = set() # columns that are already have queens
    used_diagonal1 = set() # row-col
    used_diagonal2 = set() # row + col


    solution = []

    def place_queen(row):

        # jesi all rows are filled , we found the solution
        if row == n:
            solution.append(["".join(r) for r in board])
            return

        for col in range(n):
            # check if queen is attacking 
            if(col in used_cols or
               (row - col ) in used_diagonal1 or 
               (row + col ) in used_diagonal2):
                    continue

# place the queen
            board[row][col] = "Q "
            used_cols.add(col)
            used_diagonal1.add(row-col)
            used_diagonal2.add(row+col)

# Move to next row 
            place_queen(row+1)

#Backtrack(remove queen)

            board[row][col] = ". "
            used_cols.remove(col)
            used_diagonal1.remove(row-col)
            used_diagonal2.remove(row+col)

    place_queen(0)
    return solution


solution = solve_n_Queens(4)

for sol in solution:
    for row in sol:
        print(row)
    print()