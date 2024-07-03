from statistics import mean

class Interval:
    def __init__(self, inferior_limit: int, superior_limit: int, absolute_frequency: int):
        self.__inferiorLimit = inferior_limit
        self.__superiorLimit = superior_limit
        self.__absoluteFrequency = absolute_frequency
        self.__accumulated_frequency = 0
        self.__relative_frequency = 0

    def calculate_mean(self):
        return mean([self.__inferiorLimit, self.__superiorLimit])

    def calculate_value(self):
        return self.calculate_mean() * self.__absoluteFrequency

    def calculate_accumulated_frequency(self, accumulated_frequency: int):
        self.__accumulated_frequency = accumulated_frequency

    def calculate_relative_frequency(self, total: int):
        self.__relative_frequency = round(self.__absoluteFrequency / total  * 100, 2)

    def absolute_frequency(self):
        return self.__absoluteFrequency

    def inferior_limit(self):
        return self.__inferiorLimit

    def superior_limit(self):
        return self.__superiorLimit

    def accumulated_frequency(self):
        return self.__accumulated_frequency

    def relative_frequency(self):
        return self.__relative_frequency
