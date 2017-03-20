# Day 8
# Turn on screen and rotate rows/columns according to commands

from day0 import *
from matplotlib import pyplot as plt

class TwoFactor:

    def __init__(self):
        self.screen = np.zeros([6, 50])
        lines = parse(8)
        print(lines)
        self.cmds = [parse_cmd(line) for line in lines]
        print(len(self.cmds))
        print(self.cmds)

    def execute_cmd(self, cmd):
        if cmd[0] == 'T':
            for i in range(int(cmd[1][1])):
                for j in range(int(cmd[1][0])):
                    self.screen[i][j] = 1
        elif cmd[0] == 'R':
            self.screen[cmd[1][0], :] = np.roll(self.screen[int(cmd[1][0]), :], int(cmd[1][1]))
        elif cmd[0] == 'C':
            self.screen[:, int(cmd[1][0])] = np.roll(self.screen[:, int(cmd[1][0])], int(cmd[1][1]))

    def run(self):
        for cmd in self.cmds:
            self.execute_cmd(cmd)
        print(self.screen)
        return np.sum(self.screen), self.screen


def parse_cmd(s):
    """parse list of strings which are commands, return """
    groups = re.split(r'\s', s)
    if groups[0] == 'rect':
        return 'T', re.findall(r'(\d+)x(\d+)', groups[1])[0]
    elif groups[1] == 'row':
        return 'R', (re.findall(r'(\d+)', groups[2])[0], re.findall(r'(\d+)', groups[4])[0])
    elif groups[1] == 'column':
        return 'C', (re.findall(r'(\d+)', groups[2])[0], re.findall(r'(\d+)', groups[4])[0])


if __name__ == "__main__":
    server = TwoFactor()
    num_pixels, screen = server.run()
    print(num_pixels)
    plt.imshow(screen)
    plt.show()

