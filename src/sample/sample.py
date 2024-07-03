import math

from ..interval.interval import Interval
from ..utils.mode.mode_utils import find_mode_class, apply_mode_formula


class Sample:
    def __init__(self, rol: list[int], classes_quantity: int = 0, amplitude: int = 0):
        self.__rol = rol
        self.__intervals = list[Interval]()
        self.__range = 0
        self.__amplitude = amplitude
        self.__mode = 0
        self.__mean = 0
        self.__median = 0
        self.__classes_quantity = classes_quantity

    def add_interval(self, lower_limit: int, upper_limit: int, total_frequency: int):
        self.__intervals.append(Interval(lower_limit, upper_limit, total_frequency))

    def calculate_total_elements_value(self):
        intervals_values = []
        for interval in self.__intervals:
            intervals_values.append(interval.calculate_value())
        return sum(intervals_values, 0)

    def calculate_total_elements(self):
        intervals_frequencies = []
        for interval in self.__intervals:
            intervals_frequencies.append(interval.total_frequency())
        return sum(intervals_frequencies, 0)

    def calculate_mean(self):
        mean = self.calculate_total_elements_value() / self.calculate_total_elements()
        return round(mean, 2)

    def calculate_mode(self):
        mode_class = find_mode_class(self.__intervals)
        ls = len(self.__intervals)
        before_mode_class_frequency = self.__intervals[mode_class - 1].total_frequency() if mode_class - 1 > 0 else 0
        after_mode_class_frequency = self.__intervals[mode_class + 1].total_frequency() if mode_class + 1 < ls else 0
        delta_one = self.__intervals[mode_class].total_frequency() - before_mode_class_frequency
        delta_two = self.__intervals[mode_class].total_frequency() - after_mode_class_frequency
        mode = apply_mode_formula(self.__intervals[mode_class].lower_limit(), delta_one, delta_two, 500)
        return round(mode, 2)

    def calculate_accumulated_frequency_of_each_interval(self):
        self.__intervals[0].calculate_accumulated_frequency(self.__intervals[0].total_frequency())
        for interval in self.__intervals[1:]:  # All elements but the first one(slicing)
            frequency = self.__intervals[self.__intervals.index(interval) - 1].accumulated_frequency()
            interval.calculate_accumulated_frequency(frequency + interval.total_frequency())

    def calculate_relative_frequency_of_each_interval(self):
        elements = self.calculate_total_elements()
        for interval in self.__intervals:
            interval.calculate_relative_frequency(elements)

    def calculate_amplitude(self):
        self.__amplitude = round(self.__range / self.__classes_quantity) + 1

    def calculate_range(self):
        self.__range = self.__rol[-1] - self.__rol[0]

    def calculate_classes_quantity(self):
        if len(self.__rol) >= 25:
            self.__classes_quantity = round(math.sqrt(len(self.__rol)))
        else: self.__classes_quantity = 5

    def define_intervals(self):
        # Calculates the amplitude of the first element
        lower_limit = self.__rol[0]
        upper_limit = self.__rol[0] + self.__amplitude
        absolute_frequency = sum((lower_limit <= i < upper_limit for i in self.__rol))
        self.add_interval(lower_limit, upper_limit, absolute_frequency)

        print(self.__classes_quantity)
        # Calculates the amplitude of other classes in the sample
        for a in range(self.__classes_quantity - 1):
            lower_limit += self.__amplitude
            upper_limit = lower_limit + self.__amplitude
            absolute_frequency = sum((lower_limit <= i < upper_limit for i in self.__rol))
            self.add_interval(lower_limit, upper_limit, absolute_frequency)

    def setup(self):
        self.calculate_range()
        if self.__classes_quantity == 0:
            self.calculate_classes_quantity()
        if self.__amplitude == 0:
            self.calculate_amplitude()
        self.define_intervals()
        self.calculate_accumulated_frequency_of_each_interval()
        self.calculate_relative_frequency_of_each_interval()

    def data_formatted(self):
        data_to_show = ""
        data_to_show += ">> Intervalos\n"
        for interval in self.__intervals:
            data_to_show += (f' Intervalo: {interval.lower_limit()} |- {interval.upper_limit()}\n'
                            f'  Valor: {interval.calculate_mean()}\n'
                            f'  Frequência Absoluta: {interval.total_frequency()}\n'
                            f'  Frequência Acumulada: {interval.accumulated_frequency()}\n'
                            f'  Frequência Relativa: {interval.relative_frequency()}%\n')
        data_to_show += (f'>> Amplitude das classes: {self.__amplitude}\n'
                         f'>> Range: {self.__range}\n'
                         f'>> Quantidade de classes: {self.__classes_quantity}\n'
                         f'>> Maior valor: {self.calculate_mode()}\n'
                         f'>> Média dos valores: {self.calculate_mean()}')

        return data_to_show
