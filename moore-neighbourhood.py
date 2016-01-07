#!/bin/python
# print("moore-neighbourhood")

def count_neighbours(board, row, col):
    xsize = len(board[0])
    ysize = len(board)
    count = 0
    for y in range(0, ysize):
        if (y >= (row - 1)) and (y <= (row + 1)):
            for x in range(0, xsize):
                if (x >= (col - 1)) and (x <= (col + 1)):
                    if not (x == col and y == row):
                        print(x, y)
                        if board[y][x]:
                            count = count + 1
    return count


results = []
results.append(count_neighbours(((1, 0, 0, 1, 0),
                                 (0, 1, 0, 0, 0),
                                 (0, 0, 1, 0, 1),
                                 (1, 0, 0, 0, 0),
                                 (0, 0, 1, 0, 0),), 1, 2) == 3)
results.append(count_neighbours(((1, 0, 0, 1, 0),
                                 (0, 1, 0, 0, 0),
                                 (0, 0, 1, 0, 1),
                                 (1, 0, 0, 0, 0),
                                 (0, 0, 1, 0, 0),), 0, 0) == 1)

results.append(count_neighbours(((1, 0, 1, 0, 1),
                                 (0, 1, 0, 1, 0),
                                 (1, 0, 1, 0, 1),
                                 (0, 1, 0, 1, 0),
                                 (1, 0, 1, 0, 1),
                                 (0, 1, 0, 1, 0),), 4, 4) == 2)

results.append(count_neighbours(((1, 0, 1, 0, 1),
                                 (0, 1, 0, 1, 0),
                                 (1, 0, 1, 0, 1),
                                 (0, 1, 0, 1, 0),
                                 (1, 0, 1, 0, 1),
                                 (0, 1, 0, 1, 0),), 5, 4) == 2)

print("results: ", results)
