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
        for i in range(m.width):
            if m.g(0, i) == "S":
                beam_positions[i] = 1
                break

        splits = 0
        for h in range(2, m.height, 2):
            for w in range(m.width):
                if m.g(h,w) == "^" and w in beam_positions:
                    multiplicity = beam_positions.pop(w)
                    # never 2 directly next to each other
                    # so no need for a temp buffer
                    if w-1 in beam_positions:
                        beam_positions[w-1] += multiplicity
                    else:
                        beam_positions[w-1] = multiplicity
                    if w+1 in beam_positions:
                        beam_positions[w+1] += multiplicity
                    else:
                        beam_positions[w+1] = multiplicity
                    splits += 1
        return [splits, sum(beam_positions.values())]