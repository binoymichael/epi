import random
import collections

WHITE, BLACK = range(2)
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, start, end):
    path = []

    def feasible(c):
        if (0 <= c.x < len(maze)) and (0 <= c.y < len(maze[c.x])) and maze[c.x][c.y] == WHITE:
                return True

    def search_maze_helper(current):
        if current == end:
            return True

        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next = Coordinate(current.x + x, current.y + y)
            if feasible(next):
                maze[next.x][next.y] = BLACK
                path.append(next)
                if search_maze_helper(next):
                    return True
                path.pop()

        return False

    path.append(start)
    maze[start.x][start.y] = BLACK
    search_maze_helper(start)
    return path




def main():
    for _ in range(1):
        n = 5
        m = 5
        maze = [[random.randrange(2) for _ in range(m)] for _ in range(n)]
        white = []
        for i in range(n):
            for j in range(m):
                if maze[i][j] == WHITE:
                    white.append(Coordinate(i, j))
            print(*maze[i])
        print()
        if white:
            start = random.randrange(len(white))
            end = random.randrange(len(white))
            print(white[start].x, white[start].y)
            print(white[end].x, white[end].y)
            path = search_maze(maze, white[start], white[end])
            print(path)
            if path:
                assert white[start] == path[0] and white[end] == path[-1]
            for i in range(len(path)):
                print('(%d,%d)' % path[i])
                if i > 0:
                    assert abs(path[i - 1].x - path[i].x) + abs(path[i - 1].y -
                                                                path[i].y) == 1


if __name__ == '__main__':
    main()