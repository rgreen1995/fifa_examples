import pytest
import numpy as np
import shine.analysis as analysis


@pytest.fixture()
def init_data():
    data = np.arange(10)
    return data


def test_template_func_multiply_by_two(init_data):
    doubled_data = analysis.template_func_multiply_by_two(init_data)
    expected_data = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    assert len(doubled_data) == len(init_data)
    np.testing.assert_almost_equal(doubled_data, expected_data, 5)


def test_divide_by_two(init_data):
    halved_data = analysis.divide_by_two(init_data)
    expected_data = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
    assert len(halved_data) == len(init_data)
    np.testing.assert_allclose(halved_data, expected_data)
