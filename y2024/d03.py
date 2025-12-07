import day
import re
class Day(day.Day):
    def p1(self):
        sums = 0
        matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))", self.input)
        for match in matches:
            sums += int(match[1]) * int(match[2])
        return sums

    def p2(self):
        sums = 0
        matches = re.findall(r"((mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\))", self.input)
        enabled = True
        for match in matches:
            if match[4] == "do":
                enabled = True
            elif match[5] == "don't":
                enabled = False
            elif match[1] == "mul" and enabled:
                sums += int(match[2]) * int(match[3])
        return sums
