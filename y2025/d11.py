import day, functools
class Day(day.Day):
    def p1(self): return self.run("you", 1, 1)
    def p2(self): return self.run("svr", 0, 0)
    @functools.lru_cache(None)
    def recursion(self, to_check, dac, fft):
        if "out" in self.map[to_check]: return dac and fft
        return sum(self.recursion(i, i == "dac" or dac, i == "fft" or fft) for i in self.map[to_check])
    def run(self, start, dac, fft):
        self.map = {l.split(": ")[0]: l.split(": ")[1].split(" ") for l in self.lines}
        return self.recursion(start, dac, fft)