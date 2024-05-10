def generate_cnf(grid):
    cnf = []

    rows = len(grid)
    cols = len(grid[0])

    # Lấy các ô liền kề
    def get_adjacent_cells(row, col):
        adjacent = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (dr != 0 or dc != 0) and 0 <= row + dr < rows and 0 <= col + dc < cols:
                    adjacent.append((row + dr, col + dc))
        return adjacent

    # Lặp lại từng ô
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]

            # ô trống thì bỏ qua  
            if cell == '_':
                continue

            # ô chứa số thì thêm ràng buộc
            if isinstance(cell, int):
                adjacent_cells = get_adjacent_cells(row, col)
                print(adjacent_cells   )
                trap_count = sum(1 for r, c in adjacent_cells if grid[r][c] == 'T')

                # thêm ràng buộc về số bẫy quanh ô này
                cnf.append([f"-{row*cols + col + 1}"] + [f"{(r*cols + c) + 1}" for r, c in adjacent_cells if grid[r][c] == 'T'])
                cnf.append([f"{row*cols + col + 1}"] + [f"-{(r*cols + c) + 1}" for r, c in adjacent_cells if grid[r][c] == 'T'])
                cnf.append([f"{row*cols + col + 1}"] * (trap_count - cell) + [f"-{(row*cols + col + 1)}"] * (cell - trap_count))

    return cnf

grid = [
    [3, '_', 2, '_'],
    ['_', '_', 2, '_'],
    ['_', 3, 1, '_']
]

cnf = generate_cnf(grid)
for clause in cnf:
    print(clause)
