import matplotlib.pyplot as plt

SIZE = 10 ** 4


class Solution:

    def __init__(self, g, M, m):
        self.nums = [m / M for m in self._gen_m(g, M, m)]

    @staticmethod
    def _gen_m(g, M, m):
        for _ in range(SIZE):
            m = (g * m) % M
            yield m

    def hist(self, name):
        plt.hist(self.nums, color='blue', edgecolor='black', bins=int(100/1))
        plt.title('Histogram ' + name)
        plt.show()


if __name__ == '__main__':
    A = 13, 17, 3
    B = 5 ** 17, 2 ** 42, 1
    Solution(*A).hist('Task 1(A)')
    Solution(*B).hist('Task 1(B)')
