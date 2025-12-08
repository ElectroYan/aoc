import os
import copy
import math
class Matrix:
    def __init__(self, data: list[list[object] | str] = [], height: int = 0, width: int = 0, default:object = 0):
        if data == [] and (height <= 0 or width <= 0):
            raise Exception()

        if data != []:
            if isinstance(data[0], str):
                self.data = [list(l) for l in data]
            else:
                self.data = data
            self.height = len(data)
            self.width = len(data[0])
        else:
            self.data = []
            self.height = height
            self.width = width
            for _ in range(height):
                self.data.append([default for _ in range(width)])

    def around(self, h: int, w: int, search:object = None, center: bool = False, none: bool = False, oob: bool = False) -> tuple[list[object], int] | None:
        if not self.valid(h, w) and not oob:
            return None
        res = []
        for hi in [h-1, h, h+1]:
            for wi in [w-1, w, w+1]:
                if not center and hi == h and wi == w:
                    continue
                val = self.g(hi, wi)
                if val is not None or none:
                    res.append(val)
        cnt = len(res) if not search else len([i for i in res if i == search])
        return res, cnt

    def g(self, h: int, w: int) -> object|None:
        if self.valid(h, w):
            return self.data[h][w]
        return None

    def gv(self, pos: "Vector2d") -> object|None:
        return self.g(pos.h, pos.w)

    def s(self, h: int, w: int, val) -> bool:
        if self.valid(h, w):
            self.data[h][w] = val
            return True
        return False

    def sv(self, pos: "Vector2d", val) -> bool:
        return self.s(pos.h, pos.w, val)

    def valid(self, h: int, w: int):
        return h >= 0 and h < self.height and w >= 0 and w < self.width

    def copy(self):
        return Matrix(data=copy.deepcopy(self.data))

    def find(self, func):
        occurences = []
        for h in range(self.height):
            for w in range(self.width):
                val = self.g(h,w)
                if func(h, w, val):
                    occurences.append((h,w,val,))
        return occurences

    def __str__(self, align: bool = True):
        min_size = 1
        if align:
            for i in range(self.height):
                for j in range(self.width):
                    min_size = max(min_size, len(str(self.data[i][j])))
        str_ = ""
        for i in range(self.height):
            for j in range(self.width):
                val = str(self.data[i][j])
                str_ += val.rjust(min_size + 1)
            str_ += os.linesep
        return str_

class Vector2d:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def copy(self):
        return Vector2d(self.h, self.w)

    def __add__(self, o: "Vector2d"):
        return Vector2d(self.h + o.h, self.w + o.w)

    def __str__(self):
        return str((self.h, self.w,))

    def __eq__(self, value):
        return self.h == value.h and self.w == value.w

    def __hash__(self):
        return (self.h, self.w).__hash__()

class Vector3d:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def euclid(self, o: "Vector3d") -> int:
        sub_h = self.h - o.h
        sub_w = self.w - o.w
        sub_d = self.d - o.d
        return math.sqrt(sub_h * sub_h + sub_w * sub_w + sub_d * sub_d)


    def copy(self):
        return Vector3d(self.h, self.w, self.d)

    def __add__(self, o: "Vector3d"):
        return Vector3d(self.h + o.h, self.w + o.w, self.d + o.d)

    def __str__(self):
        return str((self.h, self.w, self.d,))

    def __eq__(self, value):
        return self.h == value.h and self.w == value.w and self.d == value.d

    def __hash__(self):
        return (self.h, self.w, self.d).__hash__()

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    m = Matrix(height=3, width=4)
    m.s(2,1, 1000)
    print(m)
    print(m.around(-1,1, none = True, include=True, oob = True))