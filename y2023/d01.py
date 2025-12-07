import day
import re
class Day(day.Day):
    def p1(self):
        s = 0
        for l in self.lines:
            li = re.sub("[^0-9]", "", l)
            if li != "":
                s += int(li[0]) * 10 + int(li[-1])
        return s

    def p2(self): # new
        s = 0
        n = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
        n_rev = "".join(list(n).__reversed__())
        match = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        for l in self.lines:
            li_left = l
            li_right = "".join(list(l).__reversed__())

            m_left = re.search("("+n+")", li_left)
            m_right = re.search("("+n_rev+")", li_right)

            s += match[m_left.group(1)] * 10 + match["".join(list(m_right.group(1)).__reversed__())]
        return s
