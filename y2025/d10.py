import day
import re
import pulp
import numpy
class Day(day.Day):
    def p1(self):
        inp = self.parse()

        s = 0
        for i in inp:
            s += self.solve1(i)
        return s

    def comp(self, goal, current):
        return all(i == j for i,j in zip(goal, current))

    def toggle(self, light, button):
        for i in button:
            light[i] = not light[i]
        return light

    def solve1(self, inp):
        l = inp["l"]
        valid_combinations = []
        for combination in range(2**len(inp["b"])):
            bi = "".join(list("{0:b}".format(combination)).__reversed__())
            buttons_to_press = []
            for i, x in enumerate(bi):
                if x == "1":
                    buttons_to_press.append(inp["b"][i])
            lights = [False for i in range(len(l))]
            for button in buttons_to_press:
                lights = self.toggle(lights, button)
            if self.comp(l, lights):
                valid_combinations.append(buttons_to_press)

        return min(len(i) for i in valid_combinations)

    def p2(self):
        inp = self.parse()

        s = 0
        for i in inp:
            s += self.solve2_ilp(i)
        return s

    def solve2_ilp(self, inp):
        j = inp["j"]
        buttons = inp["b"]
        prob = pulp.LpProblem("MinimizeButtonPresses", pulp.LpMinimize)

        button_vars = [pulp.LpVariable(f"button_{i}", lowBound=0, cat='Integer') for i in range(len(buttons))]

        prob += pulp.lpSum(button_vars)

        for light_index in range(len(j)):
            prob += (pulp.lpSum([button_vars[button_index] for button_index, button in enumerate(buttons) if light_index in button]) == j[light_index])

        prob.solve(pulp.PULP_CBC_CMD(msg=False))

        return int(pulp.value(prob.objective))


    def is_below_or_equal(self, goal, current):
        all_equal = True
        unequal_ind = []
        equal_ind = []
        for ind, (g,c) in enumerate(zip(goal, current)):
            if c > g:
                return None, [], []
            if c < g:
                all_equal = False
                unequal_ind.append((ind, g-c))
            if c == g:
                equal_ind.append(ind)
        return all_equal, [i[0] for i in unequal_ind], equal_ind

    def button_valid(self, buttons, equ, index):
        valid = []
        for button in buttons:
            ok = True
            for i in equ:
                if i in button:
                    ok = False
                    break
            if ok and index in button:
                valid.append(button)
        return valid

    def toggle_n_times(self, current: list, button, n):
        current = current.copy()
        for b in button:
            current[b] += n
        return current

    def solve2(self, inp):
        j = inp["j"]
        current = [0 for _ in range(len(j))]
        self.recursions = [0,0,0,0]
        res = self.recursion(j, inp["b"], current, 0)
        print(res)
        print("Recursions:", self.recursions)
        return res

    def recursion(self, goal, buttons, current, toggles):
        self.recursions[0] += 1
        check, uneq, equ = self.is_below_or_equal(goal, current)
        if check is None:
            self.recursions[1] += 1
            return None
        if check == True:
            self.recursions[2] += 1
            return toggles

        ok_results = []
        self.recursions[3] += 1
        for i in uneq:
            toggle_times = goal[i] - current[i]

            valid_buttons = self.button_valid(buttons, equ, i)
            for b in valid_buttons:
                res = self.recursion(goal, buttons, self.toggle_n_times(current, b, toggle_times), toggles+toggle_times)
                if res is not None:
                    ok_results.append(res)

        if len(ok_results) > 0:
            return min(ok_results)
        return None



    def parse(self):
        parsed = []
        for l in self.lines:
            match = re.match(r"\[(.*)\]\s(\(.*\))\s\{(.*)\}", l)
            buttons = match.group(2).split(" ")
            buttons = [[int(j) for j in i.strip("()").split(",")] for i in buttons]
            a = {
                "l": [True if i == "#" else False for i in list(match.group(1))],
                "b": buttons,
                "j": [int(j) for j in match.group(3).split(",")]
            }
            parsed.append(a)
        return parsed