from statistics import mean


class Interval:
    def __init__(self, lower_limit: int, upper_limit: int, total_frequency: int):
        self.__lower_limit = lower_limit
        self.__upper_limit = upper_limit
        self.__total_frequency = total_frequency
        self.__accumulated_frequency = 0
        self.__relative_frequency = 0

    def calculate_mean(self):
        return mean([self.__lower_limit, self.__upper_limit])

    def calculate_value(self):
        return self.calculate_mean() * self.__total_frequency

    def calculate_accumulated_frequency(self, accumulated_frequency: int):
        self.__accumulated_frequency = accumulated_frequency

    def calculate_relative_frequency(self, total: int):
        self.__relative_frequency = round(self.__total_frequency / total * 100, 2)

    def total_frequency(self):
        return self.__total_frequency

    def lower_limit(self):
        return self.__lower_limit

    def upper_limit(self):
        return self.__upper_limit

    def accumulated_frequency(self):
        return self.__accumulated_frequency

    def relative_frequency(self):
        return self.__relative_frequency
