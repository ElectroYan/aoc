import day
from matrix import Matrix
class Day(day.Day):
    def p1(self):
        return self.px()[0]

    def p2(self):
        return self.px()[1]

    def px(self):
        m = Matrix(self.lines)
        beam_positions = {}
        splits = 0
        for h in range(0, m.height, 2):
            for w in range(m.width):
                if m.g(h, w) == "S":
                    beam_positions[w] = 1
                elif m.g(h,w) == "^" and w in beam_positions:
                    multiplicity = beam_positions.pop(w)
                    beam_positions[w-1] = multiplicity + beam_positions.get(w-1, 0)
                    beam_positions[w+1] = multiplicity + beam_positions.get(w+1, 0)
                    splits += 1
        return [splits, sum(beam_positions.values())]