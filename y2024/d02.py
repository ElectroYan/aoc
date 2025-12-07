import day

class Day(day.Day):
    def p1(self):
        safe = 0
        for line in self.lines:
            split = [int(n) for n in line.split(' ')]
            valid = True
            sign = None
            for a,b in zip(split, split[1:]):
                if abs(a-b) < 1 or abs(a-b) > 3:
                    valid = False
                if sign is None:
                    sign = a-b > 0
                if sign != (a-b > 0):
                    valid = False
            if valid:
                safe += 1

        return safe

    def p2(self):
        safe = 0
        for line in self.lines:
            splitog = [int(n) for n in line.split(' ')]
            for i in range(-1, len(splitog)):
                if i == -1:
                    split = splitog.copy()
                else:
                    split = splitog.copy()
                    split.pop(i)
                valid = True
                sign = None
                for a,b in zip(split, split[1:]):
                    if abs(a-b) < 1 or abs(a-b) > 3:
                        valid = False
                    if sign is None:
                        sign = a-b > 0
                    if sign != (a-b > 0):
                        valid = False
                if valid:
                    safe += 1
                    # print(line, "safe")
                    break

        return safe
