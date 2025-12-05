import day

class Day(day.Day):
    def p1(self):
        ranges_, ids = self.input.split("\n\n")

        ranges = []
        for r in ranges_.splitlines():
            ranges.append([int(i) for i in r.split("-")])

        ids_ok = 0
        for i in ids.splitlines():
            for r in ranges:
                ii = int(i)
                if ii >= r[0] and ii <= r[1]:
                    ids_ok += 1
                    break
        return ids_ok

    def p2(self):
        ranges_, _ = self.input.split("\n\n")

        ranges = []
        for r in ranges_.splitlines():
            ranges.append([int(i) for i in r.split("-")])

        ranges = sorted(ranges, key=lambda x: x[0])
        ranges_merged = []

        current_range = ranges[0]
        for r in ranges[1:]:
            if r[0] <= current_range[1]:
                if r[1] >= current_range[1]:
                    current_range[1] = r[1]
            else:
                ranges_merged.append(current_range)
                current_range = r

        ranges_merged.append(current_range)

        print(ranges_merged)
        total = 0
        for r in ranges_merged:
            total += r[1] - r[0] + 1

        return total