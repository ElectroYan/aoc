import day

class Day(day.Day):
    def p1(self):
        inp = self.parse()
        self.p1_map = inp
        self.p1_cache = {}
        if "you" in inp:
            return self.p1_recursion("you")
        return 0

    def p1_recursion(self, to_check):
        if "out" in self.p1_map[to_check]:
            return 1

        if to_check in self.p1_cache:
            return self.p1_cache[to_check]

        s = 0
        for i in self.p1_map[to_check]:
            s += self.p1_recursion(i)

        if to_check not in self.p1_cache:
            self.p1_cache[to_check] = s

        return s

    def p2_recursion(self, to_check, dac_seen, fft_seen):
        if "out" in self.p2_map[to_check]:
            if dac_seen and fft_seen:
                return 1
            else:
                return 0

        if (to_check, dac_seen, fft_seen) in self.p2_cache:
            return self.p2_cache[(to_check, dac_seen, fft_seen)]

        s = 0
        for i in self.p2_map[to_check]:
            s += self.p2_recursion(i, i == "dac" or dac_seen, i == "fft" or fft_seen)

        if (to_check, dac_seen, fft_seen) not in self.p2_cache:
            self.p2_cache[(to_check, dac_seen, fft_seen)] = s

        return s

    def p2(self):
        inp = self.parse()
        self.p2_map = inp
        self.p2_cache = {}
        return self.p2_recursion("svr", False, False)

    def parse(self):
        mapping = {}

        for l in self.lines:
            k,v = l.split(": ")
            mapping[k] = v.split(" ")
        return mapping