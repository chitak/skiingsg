from random import randint, shuffle


class Matrix:

    def __init__(self, filename):
        self.matrix = []

        lines = []
        with open(filename, 'r') as matrix_file:
            lines = matrix_file.readlines()

        self.row = int(lines[0].split(" ")[0])
        self.col = int(lines[0].split(" ")[1])
        for line in lines[1:]:
            inner = []
            for splited in line.split(" "):
                inner.append(int(splited.replace('\n', '')))
            self.matrix.append(inner)

    def get(self, x, y):
        return self.matrix[x][y]

    def up(self, x, y):
        if (y-1) < 0:
            return None
        return (x, y-1)

    def down(self, x, y):
        if (y+1) >= self.row:
            return None
        return (x, y+1)

    def left(self, x, y):
        if (x-1) < 0:
            return None
        return (x-1, y)

    def right(self, x, y):
        if (x+1) >= self.row:
            return None
        return (x+1, y)



def dfs_path(matrix, start, path=[], longest=None):
    path = path + [start]
    x, y = start
    val = matrix.get(x, y)

    # print "current path: ", path
    # print "longest: ", longest

    childs = []

    up_val = None
    up = matrix.up(x, y)
    if up is not None:
        up_val = matrix.get(up)
    if up_val is not None and up_val < val:
        childs.append(up)

    down_val = None
    down = matrix.down(x, y)
    if down is not None:
        down_val = matrix.get(down)
    if down_val is not None and down_val < val:
        childs.append(down)

    left_val = None
    left = matrix.left(x, y)
    if left is not None:
        left_val = matrix.get(left)
    if left_val is not None and left_val < val:
        childs.append(left)

    right_val = None
    right = matrix.right(x, y)
    if right is not None:
        right_val = matrix.get(right)
    if right_val is not None and right_val < val:
        childs.append(right)

    if not childs:
        new_val = []
        for node in path:
            new_val.append(matrix.get(node[0], node[1]))

        longest_val = []
        for node in longest:
            longest_val.append(matrix.get(node[0], node[1]))

        diff_path = 0
        if new_val:
            diff_path = max(new_val) - min(new_val)

        diff_longest = 0
        if longest_val:
            diff_longest = max(longest_val) - min(longest_val)

        if len(path) > len(longest):
            longest = path
        elif len(path) == len(longest):
            if diff_path >= diff_longest:
                longest = path
        return longest

    for child in childs:
        if child not in path:
            new_path = dfs_path(matrix, child, path, longest)

            new_val = []
            for node in new_path:
                new_val.append(matrix.get(node[0], node[1]))

            longest_val = []
            for node in longest:
                longest_val.append(matrix.get(node[0], node[1]))

            diff_newpath = 0
            if new_val:
                diff_newpath = max(new_val) - min(new_val)

            diff_longest = 0
            if longest_val:
                diff_longest = max(longest_val) - min(longest_val)

            if new_path is not None:
                if len(new_path) > len(longest):
                    longest = new_path
                elif len(new_path) == len(longest):
                    if diff_newpath >= diff_longest:
                        longest = new_path

    return longest


def gen_matrix(m):
    x = [randint(0, 1500) for i in range(m*m)]
    shuffle(x)

    matrix = str(m) + " " + str(m) + "\n"
    for row in range(m*m):
        if row > 0 and row % m == 0:
            matrix = matrix[:-1]
            matrix += "\n"
        matrix += str(x[row]) + " "
    return matrix[:-1]


def save(filename, matrix):
    with open(filename, 'w+') as matrix_file:
        matrix_file.write(matrix)


if __name__ == '__main__':
    # save("1000x1000.txt", gen_matrix(1000))
    # matrix = Matrix("1000x1000.txt")
    # matrix = Matrix("test.txt")
    matrix = Matrix("map.txt")

    longest = []
    for i in range(matrix.row):
        for j in range(matrix.row):
            longest = dfs_path(matrix, (i, j), [], longest)

            print i, j, longest

    for node in longest:
        print matrix.get(node[0], node[1]),
