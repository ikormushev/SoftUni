def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for i in range(2, n):
        new_row = []
        for y in range(i + 1):
            left_neighbour = 0
            left_row = i - 1
            left_col = y - 1

            if (0 <= left_row < i) and (0 <= left_col < len(triangle[i-1])):
                left_neighbour = triangle[left_row][left_col]

            right_neighbour = 0
            right_row = i - 1
            right_col = y

            if (0 <= right_row < i) and (0 <= right_col < len(triangle[i-1])):
                right_neighbour = triangle[right_row][right_col]

            neighbour_sum = left_neighbour + right_neighbour
            new_row.append(neighbour_sum)
        triangle.append(new_row)

    return triangle

