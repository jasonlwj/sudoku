board = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
	empty_sq = find_empty_sq(board)

	if not empty_sq:
		return True
	else:
		row_pos, col_pos = empty_sq

	for i in range(1, 10):
		if board_is_valid(board, i, empty_sq):
			board[row_pos][col_pos] = i

			if solve(board):
				return True

			board[row_pos][col_pos] = 0

	return False

def board_is_valid(board, num, pos):
	row_pos, col_pos = pos

	# Check row
	for i in range(len(board[row_pos])):
		if board[row_pos][i] == num and i != col_pos:
			return False

	# Check column
	for i in range(len(board)):
		if board[i][col_pos] == num and i != row_pos:
			return False

	# Check local 3x3 box
	box_row_start = (row_pos // 3) * 3
	box_col_start = (col_pos // 3) * 3

	for i in range(box_row_start, box_row_start + 3):
		for j in range(box_col_start, box_col_start + 3):
			if board[i][j] == num and (i, j) != pos:
				return False

	return True

def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print('- - - - - - - - - - - - -')

		for j in range(len(board[i])):
			if j % 3 == 0 and j != 0:
				print(' | ', end='')

			if j == len(board[i]) - 1:
				print(board[i][j])
			else:
				print(str(board[i][j]) + ' ', end='')

def find_empty_sq(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				return (i, j)  # row, col

	return None

print('Before:')
print_board(board)
solve(board)
print('After:')
print_board(board)
