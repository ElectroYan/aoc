import day
import math
class Day(day.Day):
    def p1(self):
        rotation = 50
        zero = 0
        for l in self.lines:
            direction =  -1 if l[0] == "L" else 1
            amount = int(l[1:])

            rotation = (rotation + direction * amount) % 100
            if rotation == 0:
                zero += 1

        return zero


    def p2(self):
        rotation = 50
        zero = 0
        for l in self.lines:
            direction =  -1 if l[0] == "L" else 1
            amount = int(l[1:])
            for _ in range(amount):
                rotation += direction
                rotation %= 100
                if rotation == 0:
                    zero += 1
        return zero


    def p2___(self):
        rotation = 50
        zero = 0
        for l in self.lines:
            direction =  -1 if l[0] == "L" else 1
            amount = int(l[1:])
            rotation = rotation + direction * amount
            if rotation < 0:
                zero += 1

            zero += int(amount/100)
            rotation %= 100
        return zero + self.p1()


    def p2__(self):
        rotation = 50
        zero = 0
        for l in self.lines:
            direction =  -1 if l[0] == "L" else 1
            amount = int(l[1:])
            oamount = amount
            full = amount // 100
            amount %= 100
            if l[0] == "L":
                add = -100
                if amount > rotation:
                    add = 100
                amount = 100 - amount + add
            amount += 100 * full
            print(rotation, oamount, l[0], amount, rotation + amount)

            rotation += amount
            zero += rotation // 100

            rotation %= 100
        return zero

    def p2_(self):
        rotation = 50
        zero = 0
        for l in self.lines:
            direction =  -1 if l[0] == "L" else 1
            amount = int(l[1:])
            rotation_prev = rotation
            rotation = rotation + direction * amount
            add = abs(math.floor(rotation / 100))
            if rotation_prev == 0 and direction == -1:
                add -= 1
                print(f"{direction} * {amount}: {rotation_prev} -> {rotation}: {add}")
                if add < 0:
                    add = 0
            zero += add
            if rotation == 0:
                # print(f"--{direction} * {amount}: {rotation_prev} -> {rotation}: 1")
                zero += 1
            rotation %= 100
        return zero
