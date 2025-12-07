import day
import math
class Day(day.Day):

    @staticmethod
    def group_by(array, key_func, value_func):
        group = {}
        for i in array:
            key = key_func(i)
            if key in group:
                group[key].append(value_func(i))
            else:
                group[key] = [value_func(i)]
        return group

    def p1(self):
        orderings = [
            n.split("|") for n in self.input.split("\n\n")[0].split("\n")
        ]
        updates = [
            n.split(",") for n in self.input.split("\n\n")[1].split("\n")
        ]
        anti_map = Day.group_by(orderings, lambda i: i[1], lambda i: i[0])
        valid_updates = []
        for update in updates:
            update_valid = self.check_pageordering(update, anti_map)[0]

            if update_valid:
                valid_updates.append(update)


        total = 0
        for i in valid_updates:
            total += int(i[math.floor(len(i)/2)])
        return total

    def check_pageordering(self, update, anti_map):
        for i, start in enumerate(update):
            if i == len(update) - 1: break
            for j, end in enumerate(update[i+1:]):
                if start in anti_map and end in anti_map[start]:
                    return (False, i, j + i + 1)
        return (True, 0, 0)

    def p2(self):
        orderings = [
            n.split("|") for n in self.input.split("\n\n")[0].split("\n")
        ]
        updates = [
            n.split(",") for n in self.input.split("\n\n")[1].split("\n")
        ]
        anti_map = Day.group_by(orderings, lambda i: i[1], lambda i: i[0])
        valid_updates = []
        for update in updates:
            update_valid = self.check_pageordering(update, anti_map)[0]

            if not update_valid:
                valid_updates.append(update)

        total = 0
        fixed_updates = []
        for update in valid_updates:
            swap_occured = True
            while swap_occured:
                valid = self.check_pageordering(update, anti_map)
                if valid[0]:
                    fixed_updates.append(update)
                    swap_occured = False
                else:
                    update[valid[1]], update[valid[2]] = update[valid[2]], update[valid[1]]
                    swap_occured = True
        for i in fixed_updates:
            total += int(i[math.floor(len(i)/2)])
        return total
