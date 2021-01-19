"""Module contains code to do the analysis."""
import numpy as np
import pandas as pd

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

def load_pupil_data() -> pd.core.frame.DataFrame:
    """
    Function to load Chance To Shine school pupil dataset from Sunbird storage area 
    to a Pandas DataFrame. 
    """
    df = pd.read_csv('/cdt_storage/scw1738/ChanceToShine/School_Pupil_Data/pupil_data_clean.csv', header=0)
    return df

def remove_NoVal_col(df: pd.core.frame.DataFrame, label: str) -> pd.core.series.Series:
    """
    Function to remove 99.0 No Value placeholder from a given column (key = label) 
    in a given Pandas DataFrame (df). Returns Column with No Value placeholder items 
    removed.
    
    :param df: Pandas dataframe containing column we want to remove NoVal placeholders from.
    :param label: String corresponding to the key of the column in DataFrame we want to 
                  remove NoVal placeholders from.
    """
    mask = df[label] != 99.0
    col = df[label][mask]
    return col

def remove_NaN_col(df: pd.core.frame.DataFrame, label: str) -> pd.core.series.Series:
    """
    Function to remove NaN placeholder from a given column (key = label) 
    in a given Pandas DataFrame (df). Returns Column with NaN items 
    removed.
    
    :param df: Pandas dataframe containing column we want to remove NaN placeholders from.
    :param label: String corresponding to the key of the column in DataFrame we want to 
                  remove NaN placeholders from.
    """
    mask = df[label].astype(str) != 'nan'
    col = df[label][mask]
    return col

def clean_col(df: pd.core.frame.DataFrame, label: str) -> pd.core.series.Series:
    """
    Function to remove 99.0 No Value and NaN placeholders from a given column (key = label) 
    in a given Pandas DataFrame (df). Returns Column with No Value and NaN placeholder items 
    removed.
    
    :param df: Pandas dataframe containing column we want to remove NoVal and NaN placeholders from.
    :param label: String corresponding to the key of the column in DataFrame we want to 
                  remove NoVal and NaN placeholders from.
    """
    mask = (df[label].astype(str) != 'nan') & (df[label] != 99.0)
    col = df[label][mask]
    return col

def clean_df_from_col(df: pd.core.frame.DataFrame, label: str) -> pd.core.frame.DataFrame:
    """
    Function to remove all rows from DataFrame (df) that contain a No Value
    placeholder (99.0) or a NaN placeholder in a given column (key = label).
    
    This is to allow useful comparison between column clean is based on and
    other question responses.
    
    :param df: Pandas dataframe containing our dataset.
    :param label: String corresponding to the key of the column in DataFrame we want to 
                  use as a reference to remove all rows from DataFrame that have a 
                  NoVal or NaN placeholder in this column.
    """
    mask = (df[label].astype(str) != 'nan') & (df[label] != 99.0)
    cleaned = df[mask]
    return cleaned
