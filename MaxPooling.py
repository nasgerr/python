class MaxPooling:
    def __init__(self, step=(2,2), size=(2,2)):
        self.__step = step
        self.__size = size
    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        if rows == 0:
            return [[]]
        if not all(map(lambda x: len(x) == cols, matrix)) or \
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError('Invalid matrix')

        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                res[i][j] = max(s)
        return res
