import day
from matrix import Vector2d, Matrix
class Day(day.Day):
    def p1(self):
        mat = Matrix(self.lines).copy()
        mvs = [
            Vector2d(-1, 0),
            Vector2d(0, 1),
            Vector2d(1, 0),
            Vector2d(0, -1),
        ]
        mvi = 0
        guard = mat.find(lambda _,__,i: i == "^")
        guard = Vector2d(guard[0][0], guard[0][1])

        reached_end = False

        while not reached_end:
            mat.sv(guard, "X")
            symbol = mat.gv(guard + mvs[mvi])
            if symbol is not None:
                if symbol != "#":
                    guard += mvs[mvi]
                else:
                    mvi = (mvi + 1) % 4
            else:
                reached_end = True

        return len(mat.find(lambda _, __, i: i == "X"))

    mvs = [
        Vector2d(-1, 0),
        Vector2d(0, 1),
        Vector2d(1, 0),
        Vector2d(0, -1),
    ]
    def p2(self):
        return None # Doesn't work
        mat = Matrix(self.lines).copy()
        mvi = 0
        mvs = Day.mvs
        guard = mat.find(lambda _,__,i: i == "^")
        guard = Vector2d(guard[0][0], guard[0][1])
        mat.sv(guard, ".")
        reached_end = False
        symbol_map = {
            0: "^",
            1: ">",
            2: "v",
            3: "<",
        }
        potential_blocks = []
        while not reached_end:
            if mat.gv(guard) == ".":
                mat.sv(guard, symbol_map[mvi])
            elif symbol_map[mvi] not in mat.gv(guard):
                mat.sv(guard, mat.gv(guard) + symbol_map[mvi])
            symbol = mat.gv(guard + mvs[mvi])
            if symbol is not None:
                if symbol != "#":
                    tmp_guard = guard.copy()
                    tmp_mat = mat.copy()
                    tmp_mat.sv(tmp_guard + mvs[mvi], "#")
                    tmp_mvi = mvi
                    res = self.move_until_end(tmp_mat, tmp_guard, (tmp_mvi + 1) % 4)
                    if res is not None:
                        potential_blocks.append(tmp_guard + mvs[mvi])
                    guard += mvs[mvi]
                else:
                    symbol = mat.gv(guard)
                    if symbol == ".":
                        mat.sv(guard, symbol_map[mvi] + symbol_map[(mvi + 1) % 4])
                    elif symbol_map[mvi] not in symbol:
                        mat.sv(guard, symbol + symbol_map[mvi] + symbol_map[(mvi + 1) % 4])
                    mvi = (mvi + 1) % 4
            else:
                reached_end = True
        print(mat)
        print(len(mat.find(lambda _, __, i: i != "." and i != "#")))
        return len(set(potential_blocks))

    def move_until_end(self, mat, guard, mvi):
        mvs = Day.mvs
        symbol_map = {
            0: "^",
            1: ">",
            2: "v",
            3: "<",
        }
        while True:
            if mat.gv(guard) == ".":
                mat.sv(guard, symbol_map[mvi])
            elif symbol_map[mvi] not in mat.gv(guard):
                mat.sv(guard, mat.gv(guard) + symbol_map[mvi])
            symbol = mat.gv(guard + mvs[mvi])
            if symbol is not None:
                if symbol != "#":
                    if symbol_map[mvi] in symbol:
                        return guard + mvs[mvi]
                    guard += mvs[mvi]
                else:
                    symbol = mat.gv(guard)
                    if symbol == ".":
                        mat.sv(guard, symbol_map[mvi] + symbol_map[(mvi + 1) % 4])
                    elif symbol_map[mvi] not in symbol:
                        mat.sv(guard, symbol + symbol_map[mvi] + symbol_map[(mvi + 1) % 4])
                    mvi = (mvi + 1) % 4
            else:
                return None