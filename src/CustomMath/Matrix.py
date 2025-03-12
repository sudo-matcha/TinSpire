def validate(matrix: "Matrix") -> "Matrix":
    if len(matrix.rows) == 1 or not matrix.rows:
        return matrix
    lengths = [len(row) for row in matrix.rows]
    iterator = iter(lengths)
    try:
        first = next(iterator)
    except StopIteration:
        return matrix

    for x in iterator:
        if x != first:
            return False
    return matrix

    
def dim(matrix: "Matrix") -> tuple[int,int]:
    if validate(matrix):
        dim_x = len(matrix.rows[0])
        dim_y = len(matrix.rows)
        return (dim_x, dim_y)
    else:
        return None


class Matrix:
    def __init__(self, rows: list[list[float]]=[]) -> None:
        self.rows = rows
        self = validate(self)
        # print(self)
        self.cols = [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    def __repr__(self) -> str:
        s = "Matrix [" 
        for n, row in enumerate(self.rows):
            if n > 0:
                s += (' '*8)
            for i in row:
                s +=(' ' if str(i)[0]=='-' else '  ')+str(round(i, 3))
            if n < len(self.rows) - 1:
                s += "\n"
        s += " ]\n"
        return s
        

    def negate(self) -> "Matrix":
        return Matrix([[-i for i in row] for row in self.rows])
        

    def add(self, matrix: "Matrix") -> "Matrix":
        if dim(self) != dim(matrix):
            return Matrix()

        new_rows = []

        for row_a, row_b in zip(self.rows, matrix.rows):
            new_row = []
            for a, b in zip(row_a, row_b):
                new_row.append(a+b)
            new_rows.append(new_row)

        return Matrix(new_rows)


    def sub(self, matrix: "Matrix") -> "Matrix":
        if dim(self) != dim(matrix):
            return Matrix()

        return self.add(matrix.negate())


    def scale(self, scalar: float) -> "Matrix":
        new_rows = []
        for row in self.rows:
            new_row = []
            for i in row:
                new_row.append(i * scalar)
            new_rows.append(new_row)

        return Matrix(new_rows)


    def mult(self, matrix: "Matrix") -> "Matrix":
        # print(self, matrix)
        if dim(self)[1] == dim(matrix)[0] or dim(self)[0] == dim(matrix)[1]:
        
            new_rows = []
            
            for row in self.rows:
                new_row = []
                for col in matrix.cols:
                    new_row.append(sum([i * j for i, j in zip(row, col)]))
                new_rows.append(new_row)

            return Matrix(new_rows)
        return Matrix()
        
        
