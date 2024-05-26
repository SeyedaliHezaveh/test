def countOnes(matrix):
    row = len(matrix) - 1
    col = 0
    count = 0

    while row >= 0 and col < len(matrix[0]):
        while not matrix[row][col]:
            col += 1
        count += (len(matrix[0]) - col)
        row -= 1
    return count


	
matrix = [[0, 0, 1, 1],
	[0, 0, 1, 1],
	[0, 0, 1, 1],
	[0, 1, 1, 1]];

print(countOnes(matrix))

