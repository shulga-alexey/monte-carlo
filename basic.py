import matplotlib.pyplot as plt


class Basic:
    """Базовый класс."""

    ENTRIES = 10000

    def hist(self, name=''):
        """Построить гистограмму."""
        plt.hist(self.nums, color='blue', edgecolor='black', bins=int(300/17))
        plt.title('Histogram ' + self.__class__.__name__)
        plt.show()
