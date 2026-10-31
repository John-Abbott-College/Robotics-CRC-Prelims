### Smoke and mirrors (50 points) ###

def solve(dimensions: tuple[int, int], n_pos: tuple[int, int], mirrors: list[tuple[int, int, int, int]]) -> bool:
    nx, ny = n_pos
    for mirror in mirrors:
        x1,y1,x2,y2 = mirror

        edge1 = (x1 - nx, y1-ny)
        edge2 = (x2 - nx, y2-ny)

        print(edge1)
        print(edge2)


if __name__ == "__main__":
    dimensions = (10,10)
    n_pos = (4,6)
    mirrors = [(8,1,8,6)]

    answer = solve(dimensions, n_pos, mirrors)

    print(answer)