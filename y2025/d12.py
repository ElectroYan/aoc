import day
from matrix import Matrix

class Day(day.Day):
    def p1(self):
        self.parse()
        s_max = 0
        s_min = 0
        areas_of_interest = []
        for area in self.areas:
            r_max, r_min = self.heuristic1(self.blocks, area)
            s_min += r_min
            s_max += r_max
            if r_max and not r_min:
                areas_of_interest.append(area)


        print(s_max, s_min)

        return s_min

    def heuristic1(self, blocks: list[Matrix], area: list[Matrix|int]) -> int:
        plane1 = area[0].width * area[0].height
        plane2 = (area[0].width // 3) * (area[0].height // 3) * 9
        size = [len(b.find(lambda h,w,v: v == "#")) for b in blocks]
        for i, amount in enumerate(area[1:]):
            plane1 -= size[i-1] * amount
            plane2 -= 9 * amount

        return plane1 >= 0, plane2 >= 0

    # Wanted to get a sense for the result space
    # Didn't really know how to continue
    # So checked the subreddit for hints and saw that it's easier than the test cases
    # I hesitated submitting the lower bound, but it was correct
    # Well...


    def p2(self):
        pass

    def parse(self):
        self.blocks = []
        self.areas = []
        for block in self.input.split("\n\n"):
            lines = block.split("\n")
            if lines[0][-1] == ":":
                name = lines[0][:-1]
                present = Matrix(lines[1:])
                self.blocks.append(present)
            else:
                for l in lines:
                    h,w = l.split(":")[0].split("x")
                    amount = [int(x) for x in l.split(": ")[1].split(" ")]
                    self.areas.append([Matrix(height=int(h), width=int(w), default="."), *amount])
