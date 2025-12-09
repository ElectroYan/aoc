import day

class Day(day.Day):
    def p1(self):
        points = []
        for l in self.lines:
            a,b = l.split(",")
            points.append((int(a),int(b),))

        areas = []
        for i, a in enumerate(points):
            for j, b in enumerate(points):
                if i > j:
                    areas.append( (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1) )

        return max(areas)

    def p2(self):
        points = []

        for l_p, l, l_n in zip([self.lines[-1]] + self.lines[:-1], self.lines, self.lines[1:] + [self.lines[0]]):
            x,y = l.split(",")
            x_p,y_p = l_p.split(",")
            x_n,y_n = l_n.split(",")
            points.append(
                (
                    int(x),
                    int(y),
                    "l" if int(x) > int(x_p) or int(x) > int(x_n) else "r",
                    "d" if int(y) < int(y_p) or int(y) < int(y_n) else "u",
                )
            )

        point_pairs = []
        for l, l_n in zip(points, points[1:] + [points[0]]):
            point_pairs.append((l,l_n,))

        areas = []
        for i, a in enumerate(points):
            for j, b in enumerate(points):
                if i > j:
                    areas.append( ( (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1), a, b ) )

        areas.sort(key=lambda x: x[0], reverse=True)
        for area, a, b in areas:
            if (a[0] < b[0] and a[2] == "l" \
            or a[0] > b[0] and a[2] == "r" \
            or a[1] < b[1] and a[2] == "u" \
            or a[1] > b[1] and a[2] == "d"):
                continue

            minx = min(a[0], b[0])
            maxx = max(a[0], b[0])
            miny = min(a[1], b[1])
            maxy = max(a[1], b[1])
            valid_area = True
            for p1,p2 in point_pairs:
                minpx = min(p1[0], p2[0])
                maxpx = max(p1[0], p2[0])
                minpy = min(p1[1], p2[1])
                maxpy = max(p1[1], p2[1])
                if a == p1 or b == p1 or a == p2 or b == p2:
                    continue
                if p1[0] > minx and p1[0] < maxx and p1[1] > miny and p1[1] < maxy:
                    valid_area = False
                    break
                if minpx <= minx and maxpx >= maxx and minpy > miny and minpy < maxy \
                or minpy <= miny and maxpy >= maxy and minpx > minx and minpx < maxx:
                    valid_area = False
                    break
            if not valid_area:
                continue

            print(area, a, b)
            return area