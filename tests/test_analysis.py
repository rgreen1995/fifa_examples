import pytest
import numpy as np
import pandas as pd
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

def test_load_pupil_data():
    loaded = load_pupil_data()
    assert loaded.shape == (9246, 27)
    assert type(loaded) == pd.core.frame.DataFrame
    
test_dict = {'col1': [1, 2, 99.0, np.nan], 'col2': [99.0, np.nan, 3, 4]}
test_df = pd.DataFrame(data=test_dict)

def test_remove_NoVal_col():
    NoVal_removed = analysis.remove_NoVal_col(test_df, 'col1')
    expected = pd.Series(data=[1.0, 2.0, np.nan], name='col1')
    assert len(NoVal_removed) == len(expected)
    np.testing.assert_almost_equal(NoVal_removed.to_numpy(), expected.to_numpy())

def test_remove_NaN_col():
    NaN_removed = analysis.remove_NaN_col(test_df, 'col1')
    expected = pd.Series(data=[1.0, 2.0, 99.0], name='col1')
    assert len(NaN_removed) == len(expected)
    np.testing.assert_almost_equal(NaN_removed.to_numpy(), expected.to_numpy())

def test_clean_col():
    clean = analysis.clean_col(test_df, 'col1')
    expected = pd.Series(data=[1.0, 2.0], name='col1')
    assert len(clean) == len(expected)
    np.testing.assert_almost_equal(clean.to_numpy(), expected.to_numpy())
    
def test_clean_df_from_col():
    clean_df = analysis.clean_df_from_col(test_df, 'col1')
    d_exp = {'col1': [1, 2], 'col2': [99.0, np.nan]}
    expected = pd.DataFrame(data=d_exp)
    assert clean_df.shape == expected.shape
    np.testing.assert_almost_equal(clean_df.to_numpy(), expected.to_numpy())
