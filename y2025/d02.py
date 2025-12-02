import day

class Day(day.Day):
    def p1(self):
        s = 0
        ranges = self.input.split(",")
        for r in ranges:
            start, end = r.split("-")
            for i in range(int(start), int(end)+1):
                string = str(i)
                length = len(string)
                if length % 2 == 1:
                    continue
                if string[:length//2] == string[length//2:]:
                    s += i
        return s


    def p2(self):
        length_map = {
            1: [],
            2: [1],
            3: [1],
            4: [1, 2],
            5: [1],
            6: [1, 2 ,3],
            7: [1],
            8: [1, 2, 4],
            9: [1, 3],
            10: [1, 2, 5],
        }
        s = 0
        ranges = self.input.split(",")
        for r in ranges:
            start, end = r.split("-")
            for i in range(int(start), int(end)+1):
                string = str(i)
                length = len(string)
                for l in length_map[length]:
                    first = string[:l]
                    ok = True
                    for n in range(1, length // l):
                        if string[n*l:(n+1)*l] != first:
                            ok = False
                            break
                    if ok:
                        s += i
                        break
        return s
