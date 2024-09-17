#!/usr/bin/env python3
"""Visualization function for different kinds of plots and data"""
from typing import Optional

import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_box_plot(df: pd.DataFrame, column: str, y_label: str = '', outliers: bool = True, step: Optional[int] = 100) -> None:
    """
    Plots a boxplot for the given data and column

    :param df: the dataframe for the plot
    :type df: pd.DataFrame

    :param column: the column to plot the box plot
    :type column: str

    :param y_label: the label to be used in the box plot
    :type y_label: str

    :param outliers: indicates if the data has outliers
    :type outliers: bool

    :param step: indicates the step size of the y-axis
    :type step: int

    :return: Nothing
    :rtype: None
    """
    plt.figure(figsize=(20, 10))
    plt.ylabel(y_label)
    plt.grid(True)

    if not outliers:
        upper = math.ceil(df[column].max() / 100) * 100
        lower = math.floor(df[column].min() / 100) * 100
        ticks = np.arange(lower, upper + step, step=step)

        plt.yticks(ticks)

    sns.boxplot(y=column, data=df, linewidth=2, color='darkblue')
