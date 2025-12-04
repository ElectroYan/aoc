import day
from matrix import Matrix

class Day(day.Day):
    def p1(self):
        m = Matrix(self.lines)
        s = 0
        for h in range(m.height):
            for w in range(m.width):
                if m.g(h,w) == "@":
                    if m.around(h,w, search="@") < 4:
                        s += 1
        return s



    def p2(self):
        m_curr = Matrix(self.lines)
        m_next = m_curr.copy()
        s = 1
        total = 0
        while s != 0:
            s = 0
            for h in range(m_curr.height):
                for w in range(m_curr.width):
                    if m_curr.g(h,w) == "@":
                        if m_curr.around(h,w, search="@") < 4:
                            s += 1
                            m_next.s(h,w,".")
            m_curr = m_next
            m_next = m_curr.copy()
            total += s
        return total
