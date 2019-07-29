final_grid = [[0,0,0,0,4,3,2,0,8],
              [2,0,0,0,0,5,1,0,0],
              [0,3,7,0,0,0,6,4,9],
              [4,0,2,0,5,0,0,0,0],
              [1,0,0,4,3,7,0,0,5],
              [0,0,0,0,6,0,7,0,4],
              [3,9,1,0,0,0,4,7,0],
              [0,0,5,3,0,0,0,0,6],
              [8,0,4,9,7,0,0,0,0]]

start_num = 1
solution_grid = [[[start_num + i for i in range(9)] for x in range(9)] for z in range(9)]

print(*final_grid, sep = '\n' )
print(" ")

# Final number elimination
def NumElim():
    for finrow in range(9):
        for fincol in range(9):
            if final_grid[finrow][fincol] != 0:
                for solnum in range(9):
                    solution_grid[finrow][fincol][solnum] = 0

#Row and column elimination
def RowColElim():
    for finrow in range(9):
        for fincol in range(9):
            if final_grid[finrow][fincol] != 0:
                for solrowcol in range(9):
                        solution_grid[solrowcol][fincol][final_grid[finrow][fincol] - 1] = 0
                        solution_grid[finrow][solrowcol][final_grid[finrow][fincol] - 1] = 0

#3x3 Grid elimination
def gridelim():
    for finrow in range(9):
        for fincol in range(9):
            if final_grid[finrow][fincol] != 0:
                if 0 <= finrow < 3:
                    if 0 <= fincol < 3:
                        for solrow in range(0,3):
                            for solcol in range(0,3):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 0 <= finrow < 3:
                    if 3 <= fincol < 6:
                        for solrow in range(0,3):
                            for solcol in range(3,6):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 0 <= finrow < 3:
                    if 6 <= fincol < 9:
                        for solrow in range(0,3):
                            for solcol in range(6,9):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 3 <= finrow < 6:
                    if 0 <= fincol < 3:
                        for solrow in range(3,6):
                            for solcol in range(0,3):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 3 <= finrow < 6:
                    if 3 <= fincol < 6:
                        for solrow in range(3,6):
                            for solcol in range(3,6):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 3 <= finrow < 6:
                    if 6 <= fincol < 9:
                        for solrow in range(3,6):
                            for solcol in range(6,9):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 6 <= finrow < 9:
                    if 0 <= fincol < 3:
                        for solrow in range(6,9):
                            for solcol in range(0,3):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 6 <= finrow < 9:
                    if 3 <= fincol < 6:
                        for solrow in range(6,9):
                            for solcol in range(3,6):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0
                if 6 <= finrow < 9:
                    if 6 <= fincol < 9:
                        for solrow in range(6,9):
                            for solcol in range(6,9):
                                solution_grid[solrow][solcol][final_grid[finrow][fincol]-1] = 0

#Find number via row col grid elimination
def finalnumcolgrid(repeat):
    rowcount = 0
    colcount = 0
    boxcount = 0
    for finrow in range(9):
        for fincol in range(9):
            if final_grid[finrow][fincol] == 0:
                for finnum in range(9):
                    if solution_grid[finrow][fincol][finnum] != 0:
                        for colcounter in range(9):
                            if solution_grid[finrow][colcounter][finnum] != 0:
                                rowcount += 1
                        for rowcounter in range(9):
                            if solution_grid[rowcounter][fincol][finnum] != 0:
                                colcount += 1
                        if 0 <= finrow < 3:
                            if 0 <= fincol < 3:
                                for solrow in range(0, 3):
                                    for solcol in range(0, 3):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 0 <= finrow < 3:
                            if 3 <= fincol < 6:
                                for solrow in range(0, 3):
                                    for solcol in range(3, 6):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 0 <= finrow < 3:
                            if 6 <= fincol < 9:
                                for solrow in range(0, 3):
                                    for solcol in range(6, 9):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 3 <= finrow < 6:
                            if 0 <= fincol < 3:
                                for solrow in range(3, 6):
                                    for solcol in range(0, 3):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 3 <= finrow < 6:
                            if 3 <= fincol < 6:
                                for solrow in range(3, 6):
                                    for solcol in range(3, 6):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 3 <= finrow < 6:
                            if 6 <= fincol < 9:
                                for solrow in range(3, 6):
                                    for solcol in range(6, 9):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 6 <= finrow < 9:
                            if 0 <= fincol < 3:
                                for solrow in range(6, 9):
                                    for solcol in range(0, 3):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 6 <= finrow < 9:
                            if 3 <= fincol < 6:
                                for solrow in range(6, 9):
                                    for solcol in range(3, 6):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if 6 <= finrow < 9:
                            if 6 <= fincol < 9:
                                for solrow in range(6, 9):
                                    for solcol in range(6, 9):
                                        if solution_grid[solrow][solcol][finnum] != 0:
                                            boxcount += 1
                        if rowcount == 1:
                            final_grid[finrow][fincol] = solution_grid[finrow][fincol][finnum]
                            rowcount = 0
                            colcount = 0
                            boxcount = 0
                            repeat += 1
                        if colcount == 1:
                            final_grid[finrow][fincol] = solution_grid[finrow][fincol][finnum]
                            rowcount = 0
                            colcount = 0
                            boxcount = 0
                            repeat += 1
                        if boxcount == 1:
                            final_grid[finrow][fincol] = solution_grid[finrow][fincol][finnum]
                            rowcount = 0
                            colcount = 0
                            boxcount = 0
                            repeat += 1
                        else:
                            rowcount = 0
                            colcount = 0
                            boxcount = 0
    return repeat

#Deduction based on two adjacent rows or columns in the same 3x3 grid that can only be a particular set of numbers

def threebythreededduc(rcount, ccount):
    deduction_grid_track_row = []
    deduction_grid_track_col = []
    deduction_grid_track_num = []
    for solrow in range( rcount*3, 3 + (rcount*3)):
        for solcol in range( ccount*3, 3 + (ccount*3)):
            for solnum in range(9):
                if solution_grid[solrow][solcol][solnum] != 0:
                    deduction_grid_track_row.append(solrow)
                    deduction_grid_track_col.append(solcol)
                    deduction_grid_track_num.append(solution_grid[solrow][solcol][solnum])
    return deduction_grid_track_row, deduction_grid_track_col, deduction_grid_track_num

def threebythreelogic():
    num_position = []
    row_position = []
    col_position = []
    for rcount in range(3):
        for ccount in range(3):
            deduction_grid_track_row = threebythreededduc(rcount,ccount)[0]
            deduction_grid_track_col = threebythreededduc(rcount,ccount)[1]
            deduction_grid_track_num = threebythreededduc(rcount,ccount)[2]
            for numcounter in range(9):
                if deduction_grid_track_num.count(numcounter + 1) == 2:
                    for i in range(len(deduction_grid_track_num)):
                        if deduction_grid_track_num[i] == numcounter + 1:
                            num_position.append(i)
                    row_position.append(deduction_grid_track_row[num_position[0]])
                    row_position.append(deduction_grid_track_row[num_position[1]])
                    col_position.append(deduction_grid_track_col[num_position[0]])
                    col_position.append(deduction_grid_track_col[num_position[1]])
                    if row_position[0] == row_position[1]:
                        for z in range(9):
                            if z != col_position[0] and z != col_position[1]:
                                solution_grid[row_position[0]][z][numcounter] = 0
                    if col_position[0] == col_position[1]:
                        for k in range(9):
                            if k != row_position[0] and k != row_position[1]:
                                solution_grid[k][col_position[0]][numcounter] = 0
                    num_position.clear()
                    row_position.clear()
                    col_position.clear()

#Working grid deduction program
'''

deduction_grid_track_row = []
deduction_grid_track_col = []
deduction_grid_track_num = []

num_position = []
row_position = []
col_position = []

for solrow in range(0, 3):
    for solcol in range(6, 9):
        for solnum in range(9):
            if solution_grid[solrow][solcol][solnum] != 0:
                deduction_grid_track_row.append(solrow)
                deduction_grid_track_col.append(solcol)
                deduction_grid_track_num.append(solution_grid[solrow][solcol][solnum])

for numcounter in range(9):
    if deduction_grid_track_num.count(numcounter + 1) == 2:
        for i in range(len(deduction_grid_track_num)):
            if deduction_grid_track_num[i] == numcounter + 1:
                num_position.append(i)
        row_position.append(deduction_grid_track_row[num_position[0]])
        row_position.append(deduction_grid_track_row[num_position[1]])
        col_position.append(deduction_grid_track_col[num_position[0]])
        col_position.append(deduction_grid_track_col[num_position[1]])
        if row_position[0] == row_position[1]:
            for z in range(9):
                if z != col_position[0] and z != col_position[1]:
                    solution_grid[row_position[0]][z][numcounter] = 0
        if col_position[0] == col_position[1]:
            for k in range(9):
                if k != row_position[0] and k != row_position[1]:
                    solution_grid[k][col_position[0]][numcounter] = 0
        num_position.clear()
        row_position.clear()
        col_position.clear()

print(*solution_grid, sep = '\n' )
print("")
'''

again = 1
while again != 0:
    NumElim()
    RowColElim()
    gridelim()
    threebythreelogic()
    again = finalnumcolgrid(0)

print(*final_grid, sep = '\n' )
print("")

