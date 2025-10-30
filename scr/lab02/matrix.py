def transpose(mat):
    if len(mat) == 0:
        return []
    if isinstance(mat, list) and all(isinstance(row, list) for row in mat) and all(isinstance(element, (int, float)) for row in mat for element in row):
        row_len = [len(row) for row in mat]
        if len(set(row_len)) != 1:
            return 'ValueError'

        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

print('transpose')
print(transpose([[2, 3, 4]]))
print(transpose([[1], [2], [3]]))
print(transpose([[2, 3], [4, 5]]))
print(transpose([]))
print(transpose([[2, 3], [4]]))


def row_sums(mat):
    if len(mat) == 0:
        return []
    if isinstance(mat, list) and all(isinstance(row, list) for row in mat) and all(isinstance(element, (int, float)) for row in mat for element in row):
        row_len = [len(row) for row in mat]
        if len(set(row_len)) != 1:
            return 'ValueError'
        return [sum(element) for element in mat]

print('row_sums')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat):
    if len(mat) == 0:
        return []
    if isinstance(mat, list) and all(isinstance(row, list) for row in mat) and all(isinstance(element, (int, float)) for row in mat for element in row):
        row_len = [len(row) for row in mat]
        if len(set(row_len)) != 1:
            return 'ValueError'
    result = []
    for col_index in range(len(mat[0])):
        sum_col = 0
        for row in mat:
            sum_col += row[col_index]
        result.append(sum_col)
    return result

print('col_sums')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-2, 2], [20, -20]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))