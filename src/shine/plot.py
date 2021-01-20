"""Module contains code to create plots."""
from typing import List, Optional

import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def make_correlation_heatmap_from_df(df: pd.DataFrame,
                                     variables: List['str'],
                                     corr_method: str,
                                     save_fig: bool = False,
                                     save_dir: Optional[str] =None) -> None :
    """

    :param df: pandas dataframe to index columns
    :param variables: variables we want to compare
    :param corr_method: method of correlation
    :param save_fig: option to save figure
    :param save_dir: location to save figure
    """
    df_only_with_vars = df[variables]
    corr_df = df_only_with_vars.corr(method=corr_method)
    sns.heatmap(corr_df, annot=True)
    if save_fig :
        plt.savefig(save_dir)