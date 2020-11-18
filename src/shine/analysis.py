"""Module contains code to do the analysis."""
import numpy as np


def template_func_multiply_by_two(data: np.ndarray) -> np.ndarray:
    """
    Multiply the given data by 2.

    :param data: an array of numbers that we want to double
    """
    return 2 * data


def divide_by_two(data: np.ndarray) -> np.ndarray:
    """
    Divide the given data by 2.

    :param data: an array of numbers that we want to halve
    """
    return 0.5 * data.astype(float)
