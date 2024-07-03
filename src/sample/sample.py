import math

from ..interval.interval import Interval
from ..utils.mode.mode_utils import find_mode_class, apply_mode_formula


class Sample:
    def __init__(self, __rol: list[int], __classes_quantity: int = 0, __amplitude: int = 0):
        self.__rol = __rol
        self.__intervals = list[Interval]()
        self.__range = 0
        self.__amplitude = __amplitude
        self.__mode = 0
        self.__mean = 0
        self.__median = 0
        self.__classes_quantity = __classes_quantity

    def add_interval(self, __inferior_limit: int, __superior_limit: int, __absolute_frequency: int):
        self.__intervals.append(Interval(__inferior_limit, __superior_limit, __absolute_frequency))

    def calculate_total_elements_value(self):
        intervals_values = []
        for interval in self.__intervals:
            intervals_values.append(interval.calculate_value())
        return sum(intervals_values, 0)

    def calculate_total_elements(self):
        intervals_frequencies = []
        for interval in self.__intervals:
            intervals_frequencies.append(interval.absolute_frequency())
        return sum(intervals_frequencies, 0)

    def calculate_mean(self):
        mean = self.calculate_total_elements_value() / self.calculate_total_elements()
        return round(mean, 2)

    def calculate_mode(self):
        mode_class = find_mode_class(self.__intervals)
        ls = len(self.__intervals)
        before_mode_class_frequency = self.__intervals[mode_class - 1].absolute_frequency() if mode_class - 1 > 0 else 0
        after_mode_class_frequency = self.__intervals[mode_class + 1].absolute_frequency() if mode_class + 1 < ls else 0
        delta_one = self.__intervals[mode_class].absolute_frequency() - before_mode_class_frequency
        delta_two = self.__intervals[mode_class].absolute_frequency() - after_mode_class_frequency
        mode = apply_mode_formula(self.__intervals[mode_class].inferior_limit(), delta_one, delta_two, 500)
        return round(mode, 2)

    def calculate_accumulated_frequency_of_each_interval(self):
        self.__intervals[0].calculate_accumulated_frequency(self.__intervals[0].absolute_frequency())
        for interval in self.__intervals[1:]:  # All elements but the first one(slicing)
            frequency = self.__intervals[self.__intervals.index(interval) - 1].accumulated_frequency()
            interval.calculate_accumulated_frequency(frequency + interval.absolute_frequency())

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
        inferior_limit = self.__rol[0]
        superior_limit = self.__rol[0] + self.__amplitude
        absolute_frequency = sum((inferior_limit <= i < superior_limit for i in self.__rol))
        self.add_interval(inferior_limit, superior_limit, absolute_frequency)

        print(self.__classes_quantity)
        # Calculates the amplitude of other classes in the sample
        for a in range(self.__classes_quantity - 1):
            inferior_limit += self.__amplitude
            superior_limit = inferior_limit + self.__amplitude
            absolute_frequency = sum((inferior_limit <= i < superior_limit for i in self.__rol))
            self.add_interval(inferior_limit, superior_limit, absolute_frequency)

    def setup(self):
        self.calculate_range()
        if self.__classes_quantity == 0:
            self.calculate_classes_quantity()
        if self.__amplitude == 0:
            self.calculate_amplitude()
        self.define_intervals()
        self.calculate_accumulated_frequency_of_each_interval()
        self.calculate_relative_frequency_of_each_interval()

    def show_main_data_formatted(self):
        data_to_show = ""
        data_to_show += (f'Range: {self.__range}\n'
                         f'Amplitude: {self.__amplitude}\n'
                         f'Quantidade de classes: {self.__classes_quantity}')
        # res = (203 < i < 206 for i in self.__rol)
        return data_to_show

    def show_data_formatted(self):
        data_to_show = ""
        data_to_show += ">> Intervalos\n"
        for interval in self.__intervals:
            data_to_show += (f' Intervalo: {interval.inferior_limit()} |- {interval.superior_limit()}\n'
                            f'  Valor: {interval.calculate_mean()}\n'
                            f'  Frequência Absoluta: {interval.absolute_frequency()}\n'
                            f'  Frequência Acumulada: {interval.accumulated_frequency()}\n'
                            f'  Frequência Relativa: {interval.relative_frequency()}%\n')
        data_to_show += (f'>> Amplitude das classes: {self.__amplitude}\n'
                         f'>> Maior valor: {self.calculate_mode()}\n'
                         f'>> Média dos valores: {self.calculate_mean()}')

        return data_to_show
