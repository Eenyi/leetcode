def spiralPrint(mat, rows, cols) -> None:
    r, c = 0, 0
    last_row, last_col = rows - 1, cols - 1
    while c <= last_col and r <= last_row:
        for right in range(c, last_col + 1):
            print(mat[r][right], end=" ")
        r += 1
        for down in range(r, last_row + 1):
            print(mat[down][last_col], end=" ")
        last_col -= 1
        if r <= last_row:
            for left in range(last_col, c - 1, -1):
                print(mat[last_row][left], end=" ")
            last_row -= 1
        if c <= last_col:
            for up in range(last_row, r - 1, -1):
                print(mat[up][c], end=" ")
            c += 1
     
        
l1 = ['a', 'b', 'c', 'd']
l2 = ['f', 'g', 'h', 'i']
l3 = ['k', 'l', 'm', 'n']

myMatrix = [l1, l2, l3]

spiralPrint(myMatrix, 3, 4)