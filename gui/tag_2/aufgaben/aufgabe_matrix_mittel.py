"""(MITTEL)

Es soll eine Klasse Matrix erstellt werden, die den Zugriff auf ein Element
sowie das Schreiben eines Elements in der Matrix wie folgt durchführt


# Create a 2x2 matrix
matrix = Matrix(2, 2)

# Zeile und Spalte angeben und Wert zuweisen
matrix[0, 0] = 1
matrix[0, 1] = 2
matrix[1, 0] = 3
matrix[1, 1] = 4

# Zeile und Spalte angeben und Wert auslesen
# print(matrix[0, 1])
# print(matrix[0, 3]) # Raise InvalidMatrixAccess-Error

# Display the matrix
print(matrix)

1 2
3 4

Hinweis: Um die Aufgabe zu lösen, muss zum Beispiel die Dunder-Methoden __setitem__
überladen werden.
"""

class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __setitem__(self, index1, index2, value1, value2):
       [[i for i in range(self.list1)] for j in range(self.list2)]
       

    
    def __getitem__(self, index1, index2):
        return self.list_of_lists[index1][index2]

    
    def __str__(self):
        result = '\n'.join('\t'.join(map(str, row)) for row in self.list_of_lists)
        return result


matrix = Matrix(2, 2)
matrix[0, 0] = 1
matrix[0, 1] = 2
matrix[1, 0] = 3
matrix[1, 1] = 4

