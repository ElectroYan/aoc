import day
import re
class Day(day.Day):
    def p1(self):
        parts = []
        for l in self.lines:
            parts.append([i for i in re.split("\s+", l) if i != ""])

        s = 0
        for i in range(len(parts[0])):
            operator = parts[-1][i]
            tmp = 1 if operator == "*" else 0
            for k in range(len(parts)-1):
                if operator == "*":
                    tmp *= int(parts[k][i])
                else:
                    tmp += int(parts[k][i])
            s += tmp
        return s

    def p2(self):
        parsed = []
        operator = ""
        parsed_tmp = []
        for l in range(len(self.lines[0])):
            if operator == "":
                operator = self.lines[-1][l]
                parsed_tmp.append(operator)

            num = ""
            for k in range(len(self.lines) - 1):
                if self.lines[k][l] != " ":
                    num += self.lines[k][l]

            if num == "":
                operator = ""
                parsed.append(parsed_tmp)
                parsed_tmp = []
            else:
                parsed_tmp.append(num)
        parsed.append(parsed_tmp)

        s = 0
        for i in parsed:
            tmp = 1 if i[0] == "*" else 0
            for k in i[1:]:
                if i[0] == "*":
                    tmp *= int(k)
                else:
                    tmp += int(k)
            s += tmp

        return s
