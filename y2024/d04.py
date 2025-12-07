import day
import re
class Day(day.Day):
    def p1(self):
        input_matrix = [list(x) for x in self.lines]
        total = 0
        for line in input_matrix:
            total += self.search_array_for_xmas(line)
            line = line.copy()
            line.reverse()
            total += self.search_array_for_xmas(line)

        transposed_matrix = Day.transpose_matrix(input_matrix)
        for line in transposed_matrix:
            total += self.search_array_for_xmas(line)
            line = line.copy()
            line.reverse()
            total += self.search_array_for_xmas(line)

        diamond_matrix = Day.diamond_matrix(input_matrix)
        for line in diamond_matrix:
            total += self.search_array_for_xmas(line)
            line.reverse()
            total += self.search_array_for_xmas(line)

        diamond_matrix_2 = Day.diamond_matrix(list(reversed(input_matrix)))
        for line in diamond_matrix_2:
            total += self.search_array_for_xmas(line)
            line.reverse()
            total += self.search_array_for_xmas(line)

        return total

    def p2(self):
        a = [list(x) for x in self.lines]
        len_row = len(a[0])
        len_col = len(a)
        total = 0
        for n in range(1, len_col - 1):
            for m in range(1, len_row - 1):
                if a[n][m] == "A" and a[n - 1][m - 1] == "M" and a[n - 1][m + 1] == "M" and a[n + 1][m - 1] == "S" and a[n + 1][m + 1] == "S"\
                or a[n][m] == "A" and a[n - 1][m - 1] == "S" and a[n - 1][m + 1] == "M" and a[n + 1][m - 1] == "S" and a[n + 1][m + 1] == "M"\
                or a[n][m] == "A" and a[n - 1][m - 1] == "S" and a[n - 1][m + 1] == "S" and a[n + 1][m - 1] == "M" and a[n + 1][m + 1] == "M"\
                or a[n][m] == "A" and a[n - 1][m - 1] == "M" and a[n - 1][m + 1] == "S" and a[n + 1][m - 1] == "M" and a[n + 1][m + 1] == "S":
                    total += 1
        return total


    def search_array_for_xmas(self, array):
        string = "".join(array)
        cnt = len(re.findall("XMAS", string))
        return cnt

    def transpose_matrix(mat):
        res_mat = []
        len_row = len(mat[0])
        len_col = len(mat)
        for n in range(len_col):
            for m in range(len_row):
                if len(res_mat) == m:
                    res_mat.append([])
                res_mat[m].append(mat[n][m])
        return res_mat

    @staticmethod
    def diamond_matrix(mat):
        res_mat = []
        len_row = len(mat[0])
        len_col = len(mat)
        for i in range(0, len_row + len_col - 1):
            tmp_row = []
            range_n_min = max(1, len_col - i)
            range_n_max = max(0, min(len_col, len_col - i + len_row - 1))
            for offset, n in enumerate(range(range_n_min - 1, range_n_max)):
                m = max(0, i - len_col + 1) + offset
                tmp_row.append(mat[n][m])
            res_mat.append(tmp_row)
        return res_mat

if __name__ == "__main__":
    print(    Day.diamond_matrix(
        [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12],
            [13,14,15],
        ]
    ))
    print(Day.diamond_matrix(Day.transpose_matrix(
          [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12],
            [13,14,15],
        ]
    )))