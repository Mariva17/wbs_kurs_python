class InvalidMatrixAccess(Exception):
    pass


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __setitem__(self, index, value):
        row, col = index
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.data[row][col] = value
        else:
            raise InvalidMatrixAccess("Index out of range")

    def __getitem__(self, index):
        row, col = index
        try:
            return self.data[row][col]
        except IndexError:
            raise InvalidMatrixAccess("Index out of range") from None

    def __str__(self):
        result = []
        for row in self.data:
            result.append(" ".join(str(cell) for cell in row))
        return "\n".join(result)


# Create a 2x2 matrix
matrix = Matrix(2, 2)

# Set values using __setitem__
matrix[0, 0] = 1
matrix[0, 1] = 2
matrix[1, 0] = 3
matrix[1, 1] = 4

print(matrix[1, 12])

# Display the matrix
print(matrix)
