def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def print_pascals_triangle(n):
    triangle = [[1]]  
    for i in range(1, n + 1):  
        row = [1]  
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  
        row.append(1)  
        triangle.append(row)

    for row in triangle:
        print(row)

def main():
    num = get_positive_integer("Input a positive integer: ")
    print_pascals_triangle(num)

if __name__ == "__main__":
    main()
