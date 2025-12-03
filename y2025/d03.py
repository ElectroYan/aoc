import day

class Day(day.Day):
    def p1(self):
        s = 0
        for line in self.lines:
            queue = [0,0]
            nums_left = len(line)
            for c in line:
                ci = int(c)
                if ci > queue[0] and nums_left > 1:
                    queue[0] = ci
                    queue[1] = 0
                elif ci > queue[1]:
                    queue[1] = ci
                nums_left -= 1
            s += queue[0] * 10 + queue[1]
        return s

    def p2(self):
        s = 0
        bats = 12
        for line in self.lines:
            queue = []
            for _ in range(bats):
                queue.append(0)
            nums_left = len(line)
            for c in line:
                ci = int(c)
                for pos in range(bats):
                    if ci > queue[pos] and nums_left >= bats - pos:
                        queue[pos] = ci
                        for i in range(pos+1, bats):
                            queue[i] = 0
                        break

                nums_left -= 1
            string = ""
            for d in queue:
                string += str(d)
            s += int(string)
        return s
