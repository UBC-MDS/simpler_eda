import altair as alt
import numpy as np
import pandas as pd
import warnings


def numerical_plot(
    data,
    xval=None,
    yval=None,
    plot_type="scatter",
    color=None,
    title=None,
    font_size=10,
    color_scheme=None,
    x_transform=False,
    y_transorm=False,
):
    """
    This function takes in a data frame object, two numeric columns,
    and produces either a scatter or line plot to visualize the
    relationship of the two features. User can optionally change
    default arguements for plot-type, color/fill, title, size of text,
    color-scheme, and toggle log transformation for the x and y axis.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
       Input dataframe object.
    xval : str
      Variable used to represent the x-axis.
    yval : str
      Variable used to represent the y-axis.
    plot_type : str
      Variable used to represent the graphical relationship between xval and yval.
    color : str
      Variable used to set the color of the marks in the plot object.
    tilte : str
      Variable use to set the title of the plot.
    font_size  : str
      Variable use to set the size of the axis labels and title.
    x_transform : bool
      Determines whether a log transformation occurs on the x-axis.
    y_transform : bool
      Determines whether a log transformation occurs on the y-axis.
    Returns
    -------
    altair.vegalite.v3.api.Chart
      Scatter plot or Line plot of user-specified variables,
      along with summary statisitics such as mean, median and variance.
    Examples
    --------
    >>> from simpler_eda.numerical_eda import numerical_plot
    >>> from vega_datasets import data
    >>> numerical_plot(data.cars(), xval = "Horsepower", yval = "Acceleration", plot_type = "line",
                 color = "Origin",
                 title = " Horsepower vs Acceleration",
                 font_size = 10)
    """