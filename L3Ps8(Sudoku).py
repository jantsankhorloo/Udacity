def check_sudoku(p):
    n = len(p) #extract the size of the grid
    digit = 1 #the digit in the grid
    while digit <= n: #go through each digit
        i = 0
        while i < n: #go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n: #for each entry in i th row and column
                if p[i][j] == digit: #check row count
                    row_count += 1
                if p[j][i] == digit:
                    col_count += 1
                j += 1
            if row_count != 1 or col_count != 1:
                return False
            i += 1 #check next row and column
        digit += 1 #check next digit
    return True #nothing was wrong with the Sudoku
                
