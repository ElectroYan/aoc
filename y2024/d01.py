import day

class Day(day.Day):
    def p1(self):
        pairsleft = []
        pairsright = []
        for line in self.lines:
            left, right = line.split('   ')
            pairsleft.append(int(left))
            pairsright.append(int(right))

        sortedleft = sorted(pairsleft)
        sortedright = sorted(pairsright)
        sums = 0
        for a,b in zip(sortedleft, sortedright):
            sums += abs(int(b) - int(a))
        return sums

    def p2(self):
        pairsleft = []
        pairsright = []
        for line in self.lines:
            left, right = line.split('   ')
            pairsleft.append(int(left))
            pairsright.append(int(right))

        sums = 0
        for i in pairsleft:
            cntnum = len([n for n in pairsright if n == i])
            sums += cntnum * i
        return sums
