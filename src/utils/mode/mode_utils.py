from ...interval.interval import Interval


def find_mode_class(__intervals: list[Interval]) -> int:
    mode_class_index = 0
    highest_frequency = 0
    for interval in __intervals:
        if interval.absolute_frequency() >= highest_frequency:
            highest_frequency = interval.absolute_frequency()
            mode_class_index = __intervals.index(interval)
    return mode_class_index


def apply_mode_formula(__mode_class_inferior_limit: int, __delta_one: int, __delta_two: int, __amplitude: int) -> float:
    return __mode_class_inferior_limit + (__delta_one / (__delta_one + __delta_two)) * __amplitude
