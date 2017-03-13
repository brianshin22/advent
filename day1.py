# Day 1

from day0 import *
N, S, E, W = 1j, -1j, 1, -1


class Santa:
    def __init__(self, data_bytes):
        self.heading = N
        self.position = complex(0, 0)
        self.cmd_list = parse(data_bytes)
        self.visited = {(self.position.real, self.position.imag)}

    def step(self, cmd):
        """Step through one command, adjusting current heading and position"""
        direction, num = cmd[0], int(cmd[1])
        print(num)
        if direction == 'L':
            self.heading *= N
        else:
            self.heading *= S
        print("Current heading: ")
        print(self.heading)
        self.position += (num * self.heading)
        print("Current position: ")
        print(self.position)

    def run(self):
        """Run first part to determine how far away we end up from starting point"""
        for cmd in self.cmd_list:
            self.step(cmd)
        return distance_l1((self.position.real, self.position.imag), (0, 0))

    def run2(self):
        """Run second part to determine how far away first location we visit twice is"""
        for cmd in self.cmd_list:
            direction, num = cmd[0], int(cmd[1])
            if direction == 'L':
                self.heading *= N
            else:
                self.heading *= S
            for i in range(num):
                self.position += self.heading
                pos_tup = self.position.real, self.position.imag
                if pos_tup in self.visited:
                    return distance_l1(pos_tup, (0, 0))
                self.visited.add(pos_tup)
        return distance_l1((self.position.real, self.position.imag), (0, 0))


def parse(input_bytes):
    """return list of tuples of form (R | L, distance)"""
    return re.findall(r'(R|L)(\d+)', input_bytes)


if __name__ == "__main__":
    data = Input(1).read()
    # data = b'L2, R2, R2, R102'
    santa = Santa(data)
    #x = santa.run()
    x = santa.run2()
    print(x)





