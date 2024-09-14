#!/usr/bin/env python3
"""Defines functions for cleaning data"""
import pandas as pd


def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove outliers from a DataFrame column using the IQR method

    :param df: the dataframe to remove outliers from
    :param column: the column to remove outliers from
    :return: a DataFrame with outliers removed
    :rtype: pd.DataFrame
    """

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    df_no_outlier = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df_no_outlier
