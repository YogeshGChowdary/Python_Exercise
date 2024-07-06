# take input from user and mark in matrix where he want to hide money
# index concept used

row1 = ['🥰','🥰','🥰']
row2 = ['🥰','🥰','🥰']
row3 = ['🥰','🥰','🥰']

matrix = [row1,row2,row3]

print(row1,'\n',row2,'\n',row3)

position = input('Enter row number and column number where you want to hide money with out comma: ')

row_number = int(position[0])
column_number = int(position[1])

row_selected = matrix[row_number-1]
row_selected[column_number-1] = 'X'

print(row1,'\n',row2,'\n',row3)

