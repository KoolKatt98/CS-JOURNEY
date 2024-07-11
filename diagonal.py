def diagonal_sum(matrix):
    n = len(matrix)
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    secondary_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    return main_diagonal_sum + secondary_diagonal_sum

def main():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(diagonal_sum(matrix1))  

    matrix2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(diagonal_sum(matrix2))  

    matrix3 = [
        [2, 5, 3],
        [6, 7, 8],
        [9, 1, 4]
    ]
    print(diagonal_sum(matrix3))  

if __name__ == "__main__":
    main()
